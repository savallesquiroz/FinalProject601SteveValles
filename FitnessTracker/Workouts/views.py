from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm
from .api import get_exercises
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'workouts/home.html')


def workout_list(request):
    workouts = Workout.objects.all()
    exercises = Exercise.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts, 'exercises': exercises})



def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})


def workout_new(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('exercise_new', pk=workout.pk)  # redirect to exercise_new
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {'form': form})



def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {'form': form})


def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect('workout_list')
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})


def exercise_new(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('workout_list')  # redirect to workout_list
    else:
        form = ExerciseForm()
    return render(request, 'workouts/exercise_form.html', {'form': form})


def exercise_edit(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'workouts/exercise_edit.html', {'form': form})


def exercise_delete(request, pk, exercise_pk):
    exercise = get_object_or_404(Exercise, pk=exercise_pk)
    if request.method == "POST":
        exercise.delete()
        return redirect('workout_detail', pk=pk)
    return render(request, 'workouts/exercise_confirm_delete.html', {'exercise': exercise})


def workout_home(request):
    return render(request, 'workouts/home.html')


def edit_delete(request, workout_pk, exercise_pk):
    workout = get_object_or_404(Workout, pk=workout_pk)
    exercise = get_object_or_404(Exercise, pk=exercise_pk)
    if request.method == "POST":
        pass  # add your code here later
    else:
        workout_form = WorkoutForm(instance=workout)
        exercise_form = ExerciseForm(instance=exercise)
    return render(request, 'workouts/edit_delete_form.html', {'workout': workout, 'exercise': exercise, 'workout_form': workout_form, 'exercise_form': exercise_form})


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'workouts/exercise_detail.html', {'exercise': exercise})