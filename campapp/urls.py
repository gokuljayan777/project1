from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pogin/', views.pogin, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('college/', views.college, name='college'),
]
