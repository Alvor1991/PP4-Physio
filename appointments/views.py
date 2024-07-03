from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked successfully.')
            return render(request, 'appointments/book_appointment.html', {'form': form, 'success': True})
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'success': False})

