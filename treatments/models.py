from django.db import models
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


