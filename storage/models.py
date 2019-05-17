from django.db import models

# Create your models here.
class Roll(models.Model):
    number_of_roll = models.CharField(verbose_name='Номер рулона', max_length=20)

    def __str__(self):
        return str(self.number_of_roll)

    class Meta:
        verbose_name = 'Номер рулона'
        verbose_name_plural = 'Номера рулонов'


