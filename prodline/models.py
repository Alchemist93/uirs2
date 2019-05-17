from django.db import models
from storage.models import Roll

# Create your models here.

class RollModified(models.Model):
    number_of_roll = models.ForeignKey(Roll, on_delete=models.CASCADE, verbose_name='Номер рулона')
    number_modified = models.CharField(verbose_name='Измененный номер рулона', max_length=20)

    def __str__(self):
        return str(self.number_of_roll) + '/' + str(self.number_modified)

    class Meta:
        verbose_name = 'Измененный номер рулона'
        verbose_name_plural = 'Измененные номера рулонов'