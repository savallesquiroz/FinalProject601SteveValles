from django.shortcuts import render
from .models import Workout, Exercise

def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})
