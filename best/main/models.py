from django.db import models
from django.db.models.fields import CharField

class DietProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class BreakfastProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name


class LunchProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name


class SupperProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name
