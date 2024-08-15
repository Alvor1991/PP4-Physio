from django.shortcuts import render
from .models import Treatment, FAQ


def treatment_list(request):
    """
    View to display a list of all available treatments and FAQs.
    Retrieves all Treatment and FAQ objects from the database and
    renders them in the 'treatments/treatments.html' template.
    """
    treatments = Treatment.objects.all()
    faqs = FAQ.objects.all()
    return render(
        request,
        'treatments/treatments.html',
        {'treatments': treatments, 'faqs': faqs}
    )
