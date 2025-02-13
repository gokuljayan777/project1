from django.urls import path
from . import views
from .views import course_list 

urlpatterns = [
    path('', views.home, name='home'),
    path('pogin/', views.pogin, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('courses/', course_list, name='courses'),
    path('colleges/', views.college_list, name='college'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz_result/', views.quiz_result, name='quiz_result'),
]
