from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, max_length=254)
    phone = models.CharField(blank=False, max_length=50)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"{self.name}"
    