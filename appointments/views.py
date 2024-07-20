from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import AppointmentForm
from .models import Appointment
from .utils import get_available_time_slots
from datetime import datetime

@login_required
def book_appointment(request):
    """
    View to handle the appointment booking process, including form submission and validation.
    If the form is valid, the appointment is saved, and a success message is displayed.
    Displays an individual instance of :model:`appointments.Appointment`
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.time = datetime.strptime(form.cleaned_data['time_slot'], '%H:%M').time()
            appointment.save()
            messages.success(request, 'Your appointment has been booked successfully.')
            return render(request, 'appointments/appointment_success.html', {'appointment': appointment})
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form})


def get_time_slots(request):
    """
    View to handle AJAX requests for available time slots for a given date.
    Returns a JSON response with the available time slots.
    """
    date = request.GET.get('date')
    if date:
        available_slots = get_available_time_slots(date)
        return JsonResponse({'available_slots': available_slots})
    return JsonResponse({'available_slots': []})