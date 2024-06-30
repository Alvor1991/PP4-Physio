from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Appointment

# Create your views here.
class AppointmentList(generic.ListView):
    queryset = Appointment.objects.filter(date__gte=timezone.now()).order_by("date")
    template_name = "appointments/index.html"
    paginate_by = 6

from django.shortcuts import render, get_object_or_404
from .models import Appointment

def appointment_detail(request, id):
    """
    Display an individual :model:`appointments.Appointment`.

    **Context**

    ``appointment``
        An instance of :model:`appointments.Appointment`.

    **Template:**

    :template:`appointments/appointment_detail.html`
    """

    appointment = get_object_or_404(Appointment, id=id)

    return render(
        request,
        "appointments/appointment_detail.html",
        {"appointment": appointment},
    )
