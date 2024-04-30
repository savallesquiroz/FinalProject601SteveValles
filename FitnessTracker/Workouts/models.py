from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.user.username}\'s workout on {self.date}'

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
