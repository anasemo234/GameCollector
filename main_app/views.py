from django.shortcuts import render
# Add the following import
# from django.http import HttpResponse

# Create your views here.


# Define the home view
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# Add the Cat class & list and view function below the imports
class Game:  # Note that parens are optional if not inheriting from another class
    def __init__(self, title, genre, description, age):
        self.title = title
        self.genre = genre
        self.description = description
        self.age = age


games = [
    Game('Fifa 22', 'Sports', "Powered by Football and features groundbreaking new HyperMotion gameplay technology on PlayStation 5, Xbox Series X|S, and Stadia.", 1),
    Game('Call of Duty Warzone', 'Shooter',
         'free-to-play battle royale video game', 2),
    Game('NBA 2K22', 'Sports', 'basketball simulation video game developed by Visual Concepts and published by 2K Sports, based on the National Basketball Association', 1)

]


def games_index(request):
    return render(request, 'games/index.html', {'games': games})
