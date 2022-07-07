from django.db import models
from django.urls import reverse

# Create your models here.
OPINIONS = (
    ('L', 'Like'),
    ('D', "Don't like"),
    ('N', 'Never played')
)


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


class Review(models.Model):
    date = models.DateField('review date')
    opinion = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=OPINIONS,
        # set the default value for meal to be 'B'
        default=OPINIONS[0][0]
    )


# Create a cat_id FK
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_opinion_display()} on {self.date}"
