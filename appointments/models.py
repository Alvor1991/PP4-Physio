from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    """
    Model representing an appointment.
    Displays an individual instance of :model:`appointment.Appointment`.
    Contains client name, client email, date, time, and optional notes fields.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"
