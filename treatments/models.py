from django.db import models
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # General description
    services_offered = models.TextField(blank=True, null=True)  # Multiline HTML-friendly text
    benefits = models.TextField(blank=True, null=True)  # Multiline HTML-friendly text
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question