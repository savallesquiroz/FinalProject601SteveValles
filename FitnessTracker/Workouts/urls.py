from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.workout_home, name='workout_home'),
    path('', views.home, name='home'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/new/', views.workout_new, name='workout_new'),
    path('workouts/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('workouts/<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('workouts/<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    path('workouts/<int:pk>/exercises/<int:exercise_pk>/edit/', views.exercise_edit, name='exercise_edit'),
    path('workouts/<int:pk>/exercises/<int:exercise_pk>/delete/', views.exercise_delete, name='exercise_delete'),
    path('workouts/<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/edit/<int:pk>/', views.exercise_edit, name='exercise_edit'),
    path('exercise/delete/<int:pk>/', views.exercise_delete, name='exercise_delete'),
    path('exercise/new/', views.exercise_new, name='exercise_new'),
    path('exercise/edit/<int:pk>/', views.exercise_edit, name='exercise_edit'),
    path('workouts/<int:workout_pk>/exercises/new/', views.exercise_new, name='exercise_new'),
]
