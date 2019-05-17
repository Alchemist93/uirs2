from django.db import models

# Create your models here.

class Ral(models.Model):
    ral = models.CharField(verbose_name='RAL', max_length=20)
    ral_color = models.CharField(verbose_name='Цвет краски', max_length=20)

    def __str__(self):
        return str(self.ral)+ ' ' + str(self.ral_color)

    class Meta:
        verbose_name = 'RAL цвет'
        verbose_name_plural = 'RAL цвета'


class PaintMan(models.Model):
    paint_man = models.CharField(verbose_name='Производитель краски', max_length=20)

    def __str__(self):
        return str(self.paint_man)

    class Meta:
        verbose_name = 'Производитель краски'
        verbose_name_plural = 'Производители краски'


class SteelMan(models.Model):
    steel_man = models.CharField(verbose_name='Производитель стали', max_length=20)

    def __str__(self):
        return str(self.steel_man)

    class Meta:
        verbose_name = 'Производитель стали'
        verbose_name_plural = 'Производители стали'
