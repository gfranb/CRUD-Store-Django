from django.db import models
from categories.models import Category

# Create your models here.
class Campaing(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    