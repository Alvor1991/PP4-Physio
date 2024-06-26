from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Appointment

# Create your views here.
class AppointmentList(generic.ListView):
    queryset = Appointment.objects.filter(date__gte=timezone.now()).order_by("date")
    template_name = "appointments/index.html"
    paginate_by = 6

