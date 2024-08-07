from django.db import models
from cloudinary.models import CloudinaryField

class ClientTestimonial(models.Model):
    client_name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.testimonial_text[:50]}..."