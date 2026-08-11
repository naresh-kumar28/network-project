from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.encoding import smart_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'role', 'password', 'confirm_password')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': False},
            'phone': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password and confirm_password do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        if not username and not email:
            raise serializers.ValidationError("Either username or email is required to login.")
        if not password:
            raise serializers.ValidationError("Password is required to login.")

        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'username', 'role', 'is_active', 'created_at', 'updated_at')


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        user = self.context.get('user')
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password and confirm_password do not match."})
        return attrs

    def save(self, **kwargs):
        user = self.context.get('user')
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            
            # Reset link for frontend
            link = f"http://localhost:5173/api/user/reset/{uid}/{token}/"
            
            # Send Email Logic
            subject = "Password Reset Request - Network Management System"
            body = (
                f"Hello {user.username or user.first_name},\n\n"
                f"You requested a password reset for your account.\n"
                f"Please click the link below to reset your password:\n\n"
                f"{link}\n\n"
                f"If you did not request this, please ignore this email.\n\n"
                f"Regards,\nNetwork Project Team"
            )
            from_email = getattr(settings, 'EMAIL_HOST_USER')
            
            try:
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=from_email,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                raise serializers.ValidationError({"email": f"Failed to send email: {str(e)}"})

            attrs['user'] = user
            attrs['reset_link'] = link
            attrs['uid'] = uid
            attrs['token'] = token
            return attrs
        else:
            raise serializers.ValidationError({"email": "You are not a registered user with this email."})


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        uid = self.context.get('uid')
        token = self.context.get('token')

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Password and confirm_password do not match."})

        try:
            user_id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({"non_field_errors": "Invalid user ID or user does not exist."})

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError({"non_field_errors": "Token is invalid or expired."})

        attrs['user'] = user
        return attrs

    def save(self, **kwargs):
        user = self.validated_data['user']
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate(self, attrs):
        return attrs

    def save(self, **kwargs):
        try:
            refresh_token = self.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            raise serializers.ValidationError({"refresh": "Token is invalid or expired."})