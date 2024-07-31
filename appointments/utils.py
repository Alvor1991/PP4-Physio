from datetime import datetime, timedelta, time
from .models import Appointment

def generate_time_slots(start_time, end_time, interval):
    """
    Generate a list of time slots between start_time and end_time with a given interval.
    """
    slots = []
    current_time = start_time
    while current_time <= end_time:
        slots.append(current_time.strftime("%H:%M"))
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=interval)).time()
    return slots

def get_available_time_slots(date):
    """
    Get a list of available time slots for a given date.
    Exclude slots that have already been booked.
    """
    booked_appointments = Appointment.objects.filter(date=date).values_list('time', flat=True)
    booked_slots = [appointment.strftime("%H:%M") for appointment in booked_appointments]

    start_time = time(8, 0)  # 8:00 AM
    end_time = time(16, 0)   # 4:00 PM
    interval = 60            # 60 minutes

    all_slots = generate_time_slots(start_time, end_time, interval)
    available_slots = [slot for slot in all_slots if slot not in booked_slots]

    return available_slots