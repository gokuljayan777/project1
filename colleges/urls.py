from django.urls import path
from . import views

urlpatterns = [
    path('stc/', views.stc, name='stc'),

]
