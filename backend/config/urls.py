from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Authentication",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/v1/', include('apps.accounts.urls')),
    path('api/members/v1/', include('apps.members.urls')),
    path('api/plans/v1/', include('apps.plans.urls')),
    path('api/epins/v1/', include('apps.epins.urls')),
    path('api/network/v1/', include('apps.network.urls')),
    path('api/income/v1/', include('apps.income.urls')),
    path('api/wallet/v1/', include('apps.wallet.urls')),
    path('api/withdrawals/v1/', include('apps.withdrawals.urls')),
    path('api/sales/v1/', include('apps.sales.urls')),
    path('api/kyc/v1/', include('apps.kyc.urls')),
    path('api/notifications/v1/', include('apps.notifications.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
