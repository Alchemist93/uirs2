from django.db import models
from storage.models import Roll
from prodline.models import RollModified
from directory.models import Ral, PaintMan
from ok.models import Employee, Position

# Create your models here.


class LabTestsInputControl(models.Model):
    number_of_record = models.CharField(verbose_name='Номер записи', max_length=20)
    date = models.DateTimeField(verbose_name='Дата и время')
    roll_number = models.ForeignKey(Roll, on_delete=models.CASCADE, verbose_name='№ Рулона')
    melting_number = models.IntegerField(verbose_name='№ Плавки')
    batch_number = models.IntegerField(verbose_name='№ Партии')
    metall_thickness_in_doc = models.CharField(verbose_name='Толщина по бирке', max_length=20)
    metall_thickness_in_fact = models.CharField(verbose_name='Толщина по факту', max_length=20)
    tag_weight = models.CharField(verbose_name='Вес, кг, по бирке', max_length=20)
    tag_len = models.CharField(verbose_name='Длина, кг, по бирке', max_length=20)
    zink_adhesion = models.CharField(verbose_name='Адгезия цинка', max_length=20)
    zink_strength = models.CharField(verbose_name='Прочность на обратный удар цинка', max_length=20)
    air_humidity = models.CharField(verbose_name='Относительная влажность', max_length=20)

    def __str__(self):
        return str(self.number_of_record) + " " + str(self.date) + " " + str(self.roll_number)

    class Meta:
        verbose_name = 'Входной контроль'
        verbose_name_plural = 'Входной контроль'


class LabTestsQualityOfCleaning(models.Model):
    number_of_record = models.ForeignKey(LabTestsInputControl, on_delete=models.CASCADE, verbose_name="Номер записи")
    free_alkalinity = models.CharField(verbose_name='Свободная щелочность', max_length=20)
    total_alkalinity = models.CharField(verbose_name='Общая щелочность', max_length=20)
    pollution_coeff = models.CharField (verbose_name='Коэффициент загрязнения', max_length=20)

    def __str__(self):
        return str(self.number_of_record)

    class Meta:
        verbose_name = 'Качество моющего раствора Bonderit - C - AK 72'
        verbose_name_plural = 'Качество моющего раствора Bonderit - C - AK 72'


class Bonderit(models.Model):
    number_of_record = models.ForeignKey(LabTestsInputControl, on_delete=models.CASCADE, verbose_name="Номер записи")
    alkali_in_ml = models.CharField(verbose_name='Количество в мл', max_length=20)
    concentration = models.CharField(verbose_name='% концентрация', max_length=20)

    def __str__(self):
        return str(self.number_of_record)

    class Meta:
        verbose_name = 'Bonderit M-CR-NR'
        verbose_name_plural = 'Bonderit M-CR-NR'


class DryLayer(models.Model):
    dry_layer_thickness_1 = models.IntegerField(verbose_name='Толщина сухого слоя мкм 1 замер')
    dry_layer_thickness_2 = models.IntegerField(verbose_name='Толщина сухого слоя мкм 2 замер')
    dry_layer_thickness_3 = models.IntegerField(verbose_name='Толщина сухого слоя мкм 3 замер')
    dry_layer_thickness_sr = models.IntegerField(verbose_name='Толщина сухого слоя мкм среднее')

    class Meta:
        verbose_name = 'Толщина сухого слоя'
        verbose_name_plural = 'Толщина сухого слоя'
        abstract = True


class PrimerLayer(models.Model):
    primer_layer_thickness_1 = models.IntegerField(verbose_name='Толщина слоя грунта 1 замер')
    primer_layer_thickness_2 = models.IntegerField(verbose_name='Толщина слоя грунта 2 замер')
    primer_layer_thickness_3 = models.IntegerField(verbose_name='Толщина слоя грунта 3 замер')
    primer_layer_thickness_sr = models.IntegerField(verbose_name='Толщина слоя грунта среднее')

    class Meta:
        verbose_name = 'Толщина слоя грунта'
        verbose_name_plural = 'Толщина слоя грунта'
        abstract = True


class ReverseLayer(models.Model):
    reverse_layer_thickness_1 = models.IntegerField(verbose_name='Толщина обратного слоя мкм 1 замер')
    reverse_layer_thickness_2 = models.IntegerField(verbose_name='Толщина обратного слоя мкм 2 замер')
    reverse_layer_thickness_3 = models.IntegerField(verbose_name='Толщина обратного слоя мкм 3 замер')
    reverse_layer_thickness_sr = models.IntegerField(verbose_name='Толщина обратного слоя мкм среднее')

    class Meta:
        verbose_name = 'Толщина обратного слоя'
        verbose_name_plural = 'Толщина обратного слоя'
        abstract = True


class Brilliance(models.Model):
    brilliance_1 = models.IntegerField(verbose_name='Блеск % 1 замер')
    brilliance_2 = models.IntegerField(verbose_name='Блеск % 2 замер')
    brilliance_3 = models.IntegerField(verbose_name='Блеск % 3 замер')
    brilliance_sr = models.IntegerField(verbose_name='Блеск % среднее')

    class Meta:
        verbose_name = 'Блеск %'
        verbose_name_plural = 'Блеск %'
        abstract = True


class NotchedAdhesion(models.Model):
    notched_adhesion_1 = models.IntegerField(verbose_name='Адгезия с надрезом 1 замер')
    notched_adhesion_2 = models.IntegerField(verbose_name='Адгезия с надрезом 2 замер')
    notched_adhesion_3 = models.IntegerField(verbose_name='Адгезия с надрезом 3 замер')
    notched_adhesion_sr = models.IntegerField(verbose_name='Адгезия с надрезом среднее')

    class Meta:
        verbose_name = 'Адгезия с надрезом'
        verbose_name_plural = 'Адгезия с надрезом'
        abstract = True


class ResistanceToShock(models.Model):
    resistance_to_shock_1 = models.IntegerField(verbose_name='Стойкость к обратному удару 1 замер')
    resistance_to_shock_2 = models.IntegerField(verbose_name='Стойкость к обратному удару 2 замер')
    resistance_to_shock_3 = models.IntegerField(verbose_name='Стойкость к обратному удару 3 замер')
    resistance_to_shock_sr = models.IntegerField(verbose_name='Стойкость к обратному удару среднее')

    class Meta:
        verbose_name = 'Стойкость к обратному удару'
        verbose_name_plural = 'Стойкость к обратному удару'
        abstract = True


class AbrasionResistance(models.Model):
    abrasion_resistance_1 = models.IntegerField(verbose_name='Стойкость к истиранию 1 замер')
    abrasion_resistance_2 = models.IntegerField(verbose_name='Стойкость к истиранию 2 замер')
    abrasion_resistance_3 = models.IntegerField(verbose_name='Стойкость к истиранию 3 замер')
    abrasion_resistance_sr = models.IntegerField(verbose_name='Стойкость к истиранию среднее')

    class Meta:
        verbose_name = 'Стойкость к истиранию'
        verbose_name_plural = 'Стойкость к истиранию'
        abstract = True


class PencilHardness(models.Model):
    pencil_hardness_1 = models.IntegerField(verbose_name='Прочность по карандашу 1 замер')
    pencil_hardness_2 = models.IntegerField(verbose_name='Прочность по карандашу 2 замер')
    pencil_hardness_3 = models.IntegerField(verbose_name='Прочность по карандашу 3 замер')
    pencil_hardness_sr = models.IntegerField(verbose_name='Прочность по карандашу среднее')

    class Meta:
        verbose_name = 'Прочность по карандашу'
        verbose_name_plural = 'Прочность по карандашу'
        abstract = True


class Eriksen(models.Model):
    eriksen_1 = models.IntegerField(verbose_name='Прочность по Эриксену 1 замер')
    eriksen_2 = models.IntegerField(verbose_name='Прочность по Эриксену 2 замер')
    eriksen_3 = models.IntegerField(verbose_name='Прочность по Эриксену 3 замер')
    eriksen_sr = models.IntegerField(verbose_name='Прочность по Эриксену среднее')

    class Meta:
        verbose_name = 'Прочность по Эриксену'
        verbose_name_plural = 'Прочность по Эриксену'
        abstract = True


class ColorStandart(models.Model):
    color_standart_1 = models.IntegerField(verbose_name='Стандарт цвета 1 замер')
    color_standart_2 = models.IntegerField(verbose_name='Стандарт цвета 2 замер')
    color_standart_3 = models.IntegerField(verbose_name='Стандарт цвета 3 замер')
    color_standart_sr = models.IntegerField(verbose_name='Стандарт цвета среднее')

    class Meta:
        verbose_name = 'Стандарт цвета'
        verbose_name_plural = 'Стандарт цвета'
        abstract = True


class LabTests(DryLayer, PrimerLayer, ReverseLayer, Brilliance, NotchedAdhesion,
               ResistanceToShock, AbrasionResistance, PencilHardness, Eriksen, ColorStandart, models.Model):
    roll_number = models.ForeignKey(RollModified, on_delete=models.CASCADE, verbose_name='Номер рулона')
    ral = models.ForeignKey(Ral, on_delete=models.CASCADE, verbose_name='RAL')
    paint_man = models.ForeignKey(PaintMan, on_delete=models.CASCADE, verbose_name='Производитель краски')
    flexural_strength = models.CharField(verbose_name='Прочность при изгибе', max_length=20)
    total_thickness = models.CharField(verbose_name='Общая толщина', max_length=20)
    mass_finished = models.CharField(verbose_name='Масса готовой продукции', max_length=20)
    len_finished = models.CharField(verbose_name='Длина готовой продукции', max_length=20)
    name_of_assistant = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Имя лаборанта')
    comment = models.CharField(verbose_name='Примечания', max_length=20)

    def __str__(self):
        return (str(self.roll_number) + ' ' + str(self.ral) + ' '
                + str(self.mass_finished) + ' ' + str(self.len_finished))

    class Meta:
        verbose_name = 'Лабораторные испытания'
        verbose_name_plural = 'Лабораторные испытания'
