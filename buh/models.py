from django.db import models
from django.urls import reverse

# Create your models here.


class Counterparty(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    adress = models.CharField(max_length=50, verbose_name='Адрес компании')
    inn = models.IntegerField(max_length=20, verbose_name='ИНН')
    rchet = models.IntegerField(max_length=50, verbose_name='Рассчетный счет')
    oked = models.IntegerField(max_length=20, verbose_name='ОКЭД')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('counterparty_detail', kwargs={'counterparty_slug': self.slug})

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Interactions(models.Model):
    name = models.ForeignKey(Counterparty, on_delete=models.CASCADE,verbose_name='Наименование')
    count = models.DecimalField(max_digits=20, verbose_name='Сумма')
    comment = models.IntegerField(max_length=600, verbose_name='Комментарий')
    scan = models.ImageField(blank=True, verbose_name='Платежка или основание')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
