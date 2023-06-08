from django.db import models
from campaings.models import Campaing

# Create your models here.    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    campaing = models.ForeignKey(Campaing, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
