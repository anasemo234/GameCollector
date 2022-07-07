from django.db import models
from django.urls import reverse

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    desciprtion = models.TextField(max_length=250)
    age = models.IntegerField()

# new code below

    def __str__(self):
        return self.title


# Add this method

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
