from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Model representing the 'About Me' section.
    Displays an individual instance of :model:`about.About`.
    Contains title, updated date, and content fields.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    """
    Model representing a contact request.
    Displays an individual instance of :model:`contact.ContactRequest`.
    Contains name, email, message, read status, and creation date fields.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
