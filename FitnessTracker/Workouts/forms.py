from django import forms
from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'duration']  # replace with your actual fields
        widgets = {
            'date': forms.DateInput(format=('%Y-%m-%d'),
                                         attrs={'class':'form-control', 'type':'date'}),
            'duration': forms.TimeInput(attrs={'type': 'time'}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']
