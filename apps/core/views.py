from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def plans(request):
    return render(request, 'plans.html')

def contact(request):
    return render(request, 'contact.html')

def benefits(request):
    return render(request, 'benefits.html')