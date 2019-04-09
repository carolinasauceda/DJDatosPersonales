from django.db import models

# Create your models here.
class DatosPersonales(models.Model):
    Num_count=models.CharField(max_length=100,primary_key=True)
    Nombre=models.CharField(max_length=20)
    Sexo=models.CharField(max_length=1)
    Edad=models.IntegerField()
    FechaNacimiento=models.DateField()
    Telefono=models.CharField(max_length=10)
    Email=models.EmailField()
    Domicilio=models.TextField()

