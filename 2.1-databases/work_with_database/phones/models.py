from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.ForeignKey
    name = models.CharField(max_length=50)
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exist = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(verbose_name='Идентификатор')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)