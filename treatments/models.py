from django.db import models

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='treatment_images/', blank=True, null=True)

    def __str__(self):
        return self.name
