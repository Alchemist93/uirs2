from django.db import models
from directory.models import SteelMan

# Create your models here.


class Roll(models.Model):
    number_of_roll = models.IntegerField(verbose_name='Номер рулона')
    roll_len = models.IntegerField(verbose_name='Длина рулона')
    roll_mass = models.IntegerField(verbose_name='Масса рулона')
    roll_man = models.ForeignKey(SteelMan, on_delete=models.CASCADE, verbose_name='Производитель')

    def __str__(self):
        return str(self.number_of_roll)

    class Meta:
        verbose_name = 'Номер рулона'
        verbose_name_plural = 'Номера рулонов'


