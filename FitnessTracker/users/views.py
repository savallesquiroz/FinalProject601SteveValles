from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def home(request):
    return render(request, 'users/home.html')


def workouts(request):
    return render(request, 'workouts/workout_list.html')


def about(request):
    return render(request, 'users/about.html')