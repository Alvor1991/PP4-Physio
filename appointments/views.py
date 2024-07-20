from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
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

    return render(request, 'appointments/book_appointment.html', {'form': form, 'success': False})

@login_required
def update_appointment(request, pk):
    """
    View to handle the appointment update process.
    Displays an individual instance of :model:`appointments.Appointment`
    """
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been updated successfully.')
            return render(request, 'appointments/appointment_success.html', {'appointment': appointment})
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/update_appointment.html', {'form': form, 'appointment': appointment})

@login_required
def delete_appointment(request, pk):
    """
    View to handle the appointment deletion process.
    Displays an individual instance of :model:`appointments.Appointment`
    """
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your appointment has been deleted successfully.')
        return redirect('home')

    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

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

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')

