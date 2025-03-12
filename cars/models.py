from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='cars/')
    class Meta:
        app_label = 'cars'

    def __str__(self):
        return f"{self.brand} {self.model} {self.price} ({self.year})"
