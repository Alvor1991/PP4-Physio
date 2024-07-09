from django.shortcuts import render
from .models import Treatment

def treatment_list(request):
    treatments = Treatment.objects.all()
    return render(request, 'treatments/treatments.html', {'treatments': treatments})
