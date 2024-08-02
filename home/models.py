from django.db import models
from cloudinary.models import CloudinaryField

class HomePageContent(models.Model):
    welcome_message = models.TextField()
    banner_image = CloudinaryField('image', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"
