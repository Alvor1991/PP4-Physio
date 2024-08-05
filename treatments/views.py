from django.shortcuts import render
from .models import Treatment, FAQ

def treatment_list(request):
    treatments = Treatment.objects.all()
    faqs = FAQ.objects.all()
    return render(request, 'treatments/treatments.html', {'treatments': treatments, 'FAQs': FAQs})
