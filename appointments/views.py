from django.shortcuts import render
from .forms import AppointmentForm

def book_appointment(request):
    success = False
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = AppointmentForm()  # Reset form after successful submission
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form, 'success': success})



