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
    View to handle appointment booking, including form submission & validation.
    If form is valid, appointment is saved, and a success message displayed.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            # Convert the selected time slot to a time object
            appointment.time = datetime.strptime(
                form.cleaned_data['time_slot'], '%H:%M'
            ).time()
            # Combine date & time, then make it aware with the correct timezone
            appointment.time = timezone.make_aware(
                datetime.combine(appointment.date, appointment.time),
                timezone.get_current_timezone()
            ).time()
            appointment.save()
            # Display success message
            messages.success(
                request, 'Your appointment has been booked successfully.'
            )
            return redirect('user_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form}
                  )


@login_required
def update_appointment(request, pk):
    """
    View to handle the appointment update process.
    Allows users to update the details of an existing appointment.
    """
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            # Display success message
            messages.success(
                request, 'Your appointment has been updated successfully.'
            )
            return redirect('user_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(
        request, 'appointments/update_appointment.html',
        {'form': form, 'appointment': appointment}
    )


@login_required
def delete_appointment(request, pk):
    """
    View to handle the appointment deletion process.
    Allows users to delete an existing appointment.
    """
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        # Display success message
        messages.success(
            request, 'Your appointment has been deleted successfully.'
        )
        # Set a flag in session to indicate an appointment was deleted
        request.session['appointment_deleted'] = True
        return redirect('user_appointments')
    return render(
        request, 'appointments/delete_appointment.html',
        {'appointment': appointment}
    )


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
    Displays a list of appointments, or a message if no appointments exist.
    """
    appointments = Appointment.objects.filter(user=request.user)

    # Check if the session flag is set
    appointment_deleted = request.session.pop('appointment_deleted', False)

    # Check if no appointments exist and add a message only if not redirected
    # from a deletion
    if not appointments.exists() and not appointment_deleted:
        messages.info(
            request,
            'You have no appointments yet. Click below to book your first '
            'appointment.'
        )

    return render(
        request, 'appointments/user_appointments.html',
        {'appointments': appointments}
    )
