from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    type_restaurant = models.CharField(max_length=100, verbose_name='Tipo de restaurante')
    address = models.TextField(verbose_name='Direccion')
    phone = models.CharField(max_length=50, verbose_name='Tel{efono')

