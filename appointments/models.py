from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model extending the built-in AbstractUser
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

# Appointment model
class Appointment(models.Model):
    client_name = models.CharField(max_length=100, default='default_name')
    client_email = models.EmailField(default='default@example.com')
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.client_name} on {self.date}"

