from django.db import models

# Create your models here.
class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()

 

