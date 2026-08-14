from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plans/', views.plans, name='plans'),
    path('contact/', views.contact, name='contact'),
    path('benefits/', views.benefits, name='benefits'),
    
    
]