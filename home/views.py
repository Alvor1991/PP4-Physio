from django.shortcuts import render
from .models import HomePageContent

def home_view(request):
    """
    View to render the home page.
    Returns the rendered home.html template with home page content.
    """
    home_content = HomePageContent.objects.first()
    return render(request, 'home/home.html', {'home_content': home_content})


