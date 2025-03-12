from django.db import models

class Car(models.Model):
    Бренд = models.CharField(max_length=100)
    Модель = models.CharField(max_length=100)
    Год = models.IntegerField()
    Цена = models.IntegerField()
    Комплектация = models.IntegerField()
    Фотография = models.ImageField(upload_to='cars/')
    class Meta:
        app_label = 'cars'

    def __str__(self):
        return f"{self.Бренд} {self.Модель} {self.Цена} {self.Комплектация} ({self.Год}) "
