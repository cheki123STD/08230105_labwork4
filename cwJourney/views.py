from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# View for the main learning journey page
def index(request):
    # Renders cwJourney/templates/index.html
    return render(request, 'index.html')

# View for the about me page
def about_me(request):
    # Renders cwJourney/templates/aboutMe.html
    return render(request, 'aboutMe.html')
