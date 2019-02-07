from django.db import models

# Create your models here.


class Counterparty(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    adress = models.CharField(max_length=50, verbose_name='Адрес компании')
    inn = models.IntegerField(max_length=20, verbose_name='ИНН')
    rchet = models.IntegerField(max_length=50, verbose_name='Рассчетный счет')
    oked = models.IntegerField(max_length=20, verbose_name='ОКЭД')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
