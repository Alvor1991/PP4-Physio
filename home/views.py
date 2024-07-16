from django.shortcuts import render
from .models import HomePageContent

def home_view(request):
    """
    View to render the home page.
    Simply returns the rendered home.html template.
    """
    home_content = HomePageContent.objects.first()
    return render(request, 'home/home.html', {'banner_image': 'path/to/your/banner_image.jpg'})


