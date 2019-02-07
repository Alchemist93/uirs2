from django.db import models
from django.urls import reverse
from ok.models import Employee

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
    date = models.DateField(verbose_name='Дата')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.date)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'


class Items(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    cost = models.DecimalField(decimal_places=2, verbose_name='Стоимость')
    provider = models.ForeignKey(Counterparty, on_delete=models.CASCADE, verbose_name='Поставщик')
    amount = models.IntegerField(max_length=6, verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class ItemInStorage(models.Model):
    submitted = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    name = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Наименование')
    amount = models.IntegerField(max_length=6, verbose_name='Количество')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.submitted) + ' ' + str(self.name) + ' ' + str(self.amount)

    class Meta:
        verbose_name = 'Переданный предмет'
        verbose_name_plural = 'Переданные предметы'




