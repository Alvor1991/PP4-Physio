from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from .forms import AppointmentForm
from .models import Appointment
from .utils import get_available_time_slots
from django.utils import timezone
from datetime import datetime

@login_required
def immediate_logout_view(request):
    """
    Log the user out immediately without confirmation.
    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))

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
            # Combine date and time and then make it aware with correct timezone
            appointment.time = timezone.make_aware(datetime.combine(appointment.date, appointment.time), timezone.get_current_timezone()).time()
            appointment.save()
            messages.success(request, 'Your appointment has been booked successfully.')
            return redirect('user_appointments')
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
            return redirect('user_appointments')
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
        return redirect('user_appointments')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

@login_required
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

@login_required
def user_appointments(request):
    """
    View to display all appointments for the logged-in user.
    """
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/user_appointments.html', {'appointments': appointments})
