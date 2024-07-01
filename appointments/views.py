from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm

def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)

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

