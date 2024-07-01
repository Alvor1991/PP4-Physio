from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm

@login_required(login_url='/accounts/login/')
def dashboard(request):
    user_appointments = Appointment.objects.filter(client=request.user).order_by("date")
    return render(request, "appointments/dashboard.html", {"appointments": user_appointments})

@login_required(login_url='/accounts/login/')
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment booked successfully.'
            )
            return redirect('dashboard')
    else:
        form = AppointmentForm()
    return render(request, "appointments/book_appointment.html", {"form": form})

@login_required(login_url='/accounts/login/')
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if appointment.client != request.user:
        messages.add_message(request, messages.ERROR, 'You are not authorized to view this appointment.')
        return redirect('dashboard')
    
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment updated successfully.'
            )
            return redirect('appointment_detail', id=appointment.id)
    else:
        form = AppointmentForm(instance=appointment)

    return render(
        request,
        "appointments/appointment_detail.html",
        {
            "appointment": appointment,
            "form": form,
        },
    )


