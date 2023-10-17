from django.db import models


class CarBrand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
