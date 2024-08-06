from django.shortcuts import render
from .models import ClientTestimonial

def home_view(request):
    """
    View to render the home page.
    Returns the rendered home.html template with testimonials.
    """
    testimonials = ClientTestimonial.objects.filter(active=True)
    return render(request, 'home/home.html', {'testimonials': testimonials})
