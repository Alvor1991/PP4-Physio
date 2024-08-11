from django.shortcuts import render
from .models import ClientTestimonial

def home_view(request):
    """
    View to render the home page.
    Returns the rendered home.html template with testimonials.
    """
    testimonials = ClientTestimonial.objects.filter(active=True)
    return render(request, 'home/home.html', {'testimonials': testimonials})

def custom_404(request, exception):
    """
    Custom 404 error handler.
    Returns the rendered 404.html template.
    """
    return render(request, '404.html', status=404)