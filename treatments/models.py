from django.db import models
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  
    services_offered = models.TextField(blank=True, null=True)  
    benefits = models.TextField(blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Book Appointment')

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question