from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import AppointmentForm
from .models import Appointment
from datetime import datetime, time

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

def get_available_time_slots(date):
    all_time_slots = [time(hour, minute) for hour in range(9, 18) for minute in (0, 30)] 
    booked_slots = Appointment.objects.filter(date=date).values_list('time', flat=True)
    available_slots = [slot for slot in all_time_slots if slot not in booked_slots]
    return available_slots

def available_time_slots_view(request):
    date = request.GET.get('date')
    if date:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        available_slots = get_available_time_slots(date)
        return JsonResponse([slot.strftime('%H:%M') for slot in available_slots], safe=False)
    return JsonResponse([], safe=False)
