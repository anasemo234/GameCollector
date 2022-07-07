from django.contrib import admin

# Register your models here.
from .models import Game, Review

# Register your models here
admin.site.register(Game)

# register the new Review Model
admin.site.register(Review)
