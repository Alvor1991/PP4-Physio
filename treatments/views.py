from django.shortcuts import render

def treatments_view(request):
    return render(request, 'treatments/treatments.html')

