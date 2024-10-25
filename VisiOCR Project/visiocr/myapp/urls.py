from django.urls import path
from . import views

urlpatterns = [
    path('', views.VisitorManagementSystem.home, name='home'),
    path('generate_pass/', views.VisitorManagementSystem.generate_pass, name='generate_pass'),
]
