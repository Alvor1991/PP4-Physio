from django.db import models
from cloudinary.models import CloudinaryField

class ClientTestimonial(models.Model):
    """
    Model to store client testimonials. Includes fields for the client's name, testimonial text, 
    active status, and the date the testimonial was added.
    """
    client_name = models.CharField(max_length=100)  
    testimonial_text = models.TextField() 
    active = models.BooleanField(default=True)  
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        """
        String representation of the ClientTestimonial model.
        Returns a string combining the client's name and the first 50 characters of the testimonial text.
        """
        return f"{self.client_name} - {self.testimonial_text[:50]}..."  
