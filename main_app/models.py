from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    desciprtion = models.TextField(max_length=250)
    age = models.IntegerField()

# new code below

    def __str__(self):
        return self.title
