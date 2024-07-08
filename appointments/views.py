from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from datetime import datetime, timedelta, time

def generate_time_slots(start_time, end_time, interval):
    slots = []
    current_time = start_time
    while current_time < end_time:
        slots.append(current_time.strftime("%H:%M"))
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=interval)).time()
    return slots

def get_available_time_slots(date):
    booked_appointments = Appointment.objects.filter(date=date).values_list('time', flat=True)
    booked_slots = [appointment.strftime("%H:%M") for appointment in booked_appointments]

    start_time = time(9, 0)
    end_time = time(17, 0)
    interval = 30

    all_slots = generate_time_slots(start_time, end_time, interval)
    available_slots = [slot for slot in all_slots if slot not in booked_slots]

    return available_slots

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
        if 'date' in request.GET:
            date = request.GET['date']
            available_slots = get_available_time_slots(date)
            form.fields['time_slot'].choices = [(slot, slot) for slot in available_slots]

    return render(request, 'appointments/book_appointment.html', {'form': form, 'success': False})


