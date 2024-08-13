from django.db import models
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    """
    Model representing a treatment offered by the business.
    Includes fields for the treatment's name, description, services offered, benefits, price, image, and button text.
    """
    name = models.CharField(max_length=100)  
    description = models.TextField() 
    services_offered = models.TextField(blank=True, null=True)  
    benefits = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)  
    image = CloudinaryField('image', blank=True, null=True) 
    button_text = models.CharField(max_length=50, default='Book Appointment')  

    def __str__(self):
        """
        String representation of the Treatment model.
        Returns the name of the treatment.
        """
        return self.name  

class FAQ(models.Model):
    """
    Model representing a frequently asked question (FAQ) and its corresponding answer.
    Includes fields for the question and the answer.
    """
    question = models.CharField(max_length=255)  
    answer = models.TextField()  

    def __str__(self):
        """
        String representation of the FAQ model.
        Returns the question text.
        """
        return self.question  