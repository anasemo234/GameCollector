from django.shortcuts import render
# Add the following import
# from django.http import HttpResponse

# Create your views here.


# Define the home view
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
