from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Add this line
    path('workouts/', views.workouts, name='workouts'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
]

