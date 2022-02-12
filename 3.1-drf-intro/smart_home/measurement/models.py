from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')


class Measurement(models.Model):
    id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата измерения')
    update_date = models.DateField(auto_now=True, verbose_name='Дата измерения')
