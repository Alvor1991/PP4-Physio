from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import AppointmentForm
from .models import Appointment
from .utils import get_available_time_slots
from datetime import datetime

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.time = datetime.strptime(form.cleaned_data['time_slot'], '%H:%M').time()
            appointment.save()
            messages.success(request, 'Your appointment has been booked successfully.')
            return redirect('book_appointment')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'success': False})

def get_time_slots(request):
    date = request.GET.get('date')
    if date:
        available_slots = get_available_time_slots(date)
        return JsonResponse({'available_slots': available_slots})
    return JsonResponse({'available_slots': []})







