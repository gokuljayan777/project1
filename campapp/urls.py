from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pogin/', views.pogin, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('colleges/', views.college_list, name='college'),
    path('colleges/', views.compare, name='college'),
   
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz_result/', views.quiz_result, name='quiz_result'),

    
]
