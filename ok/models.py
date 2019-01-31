from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse

# Create your models here.


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Citizen(models.Model):
    country = models.CharField(max_length=30, verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Employee(models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    birth_day = models.DateField(blank=True, verbose_name='Дата рождения')
    passport = models.ImageField(upload_to=image_folder, verbose_name='Скан паспорта')
    registration = models.ImageField(upload_to=image_folder, verbose_name='Скан прописки')
    citizenship = models.ForeignKey(Citizen, on_delete=models.CASCADE, verbose_name='Гражданство')
    inn = models.ImageField(upload_to=image_folder, verbose_name='ИНН')
    inps = models.ImageField(upload_to=image_folder, verbose_name='ИНПС')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.surname + ' ' + self.name + ' ' + self.patronymic)

    def get_absolute_url(self):
        return reverse('personal_detail', kwargs={'personal_slug': self.slug})

    class Meta:
        verbose_name = 'Личные данные сотрудника'
        verbose_name_plural = 'Личные данные сотрудников'


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.surname + instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Employee)


def pre_save_category(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category, sender=Category)


class Position(models.Model):
    position = models.CharField(max_length=50, verbose_name='Должность')
    depart = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Отдел')
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField(verbose_name='Дата приема')
    price = models.DecimalField(max_digits=20, verbose_name='Оклад', decimal_places=2)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


def pre_save_pos(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.position), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_pos, sender=Position)


class Vacation(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='сотрудник')
    start_vacation = models.DateField(verbose_name='начало отпуска')
    end_vacation = models.DateField(verbose_name='Конец отпуска')

    def __str__(self):
        return (str(self.user) + str(self.start_vacation) + str(self.end_vacation))

    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуска'
