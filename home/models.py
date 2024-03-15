from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    
    def __str__(self):
        return self.name