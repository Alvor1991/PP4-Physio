from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AppointmentForm

class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all().order_by("date")
    template_name = "appointments/index.html"
    paginate_by = 6

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked.')
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})
