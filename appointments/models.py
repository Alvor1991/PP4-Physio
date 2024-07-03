from django.db import models

class Appointment(models.Model):
    client_name = models.CharField(max_length=100, default='default_name')
    client_email = models.EmailField(default='default@example.com')
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.client_name} on {self.date} at {self.time}"



