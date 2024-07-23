from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Appointment(models.Model):
    """
    Model representing an appointment.
    Displays an individual instance of :model:`appointment.Appointment`.
    Contains client name, client email, date, time, and optional notes fields.
    """
    TREATMENT_CHOICES = [
        ('physio', 'Physiotherapy'),
        ('massage', 'Massage Therapy'),
        ('acupuncture', 'Acupuncture'),
        # Add more treatments as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    treatment = models.CharField(max_length=50, choices=TREATMENT_CHOICES, default='physio')

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time} for {self.treatment}"