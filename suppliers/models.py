from django.db import models

# Create your models here.

class Supplier(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    dni=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    mail=models.EmailField()