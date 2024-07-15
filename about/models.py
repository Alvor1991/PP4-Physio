from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Model to store information about the website or business, 
    including title, last updated date, and content.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class ContactRequest(models.Model):
    """
    Model to store contact requests submitted by users, 
    including their name, email, message, read status, and the date created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

