from django.db import models
from django.urls import reverse
from ok.models import Employee
from transliterate import translit
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Counterparty(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    adress = models.CharField(max_length=50, verbose_name='Адрес компании')
    inn = models.IntegerField(verbose_name='ИНН')
    rchet = models.IntegerField(verbose_name='Рассчетный счет')
    oked = models.IntegerField(verbose_name='ОКЭД')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('counterparty_detail', kwargs={'counterparty_slug': self.slug})

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


def pre_save_cp(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug

pre_save.connect(pre_save_cp, sender=Counterparty)


class Interactions(models.Model):
    name = models.ForeignKey(Counterparty, on_delete=models.CASCADE,verbose_name='Наименование')
    count = models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Сумма')
    comment = models.CharField(max_length=600, verbose_name='Комментарий')
    scan = models.ImageField(upload_to=image_folder, blank=True, verbose_name='Платежка или основание')
    date = models.DateField(verbose_name='Дата')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.date)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

pre_save.connect(pre_save_cp, sender=Interactions)

class Items(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    cost = models.DecimalField(decimal_places=2, max_digits=999, verbose_name='Стоимость')
    provider = models.ForeignKey(Counterparty, on_delete=models.CASCADE, verbose_name='Поставщик')
    amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class ItemInStorage(models.Model):
    submitted = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    name = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Наименование')
    amount = models.IntegerField(verbose_name='Количество')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.submitted) + ' ' + str(self.name) + ' ' + str(self.amount)

    class Meta:
        verbose_name = 'Переданный предмет'
        verbose_name_plural = 'Переданные предметы'

pre_save.connect(pre_save_cp, sender=ItemInStorage)


