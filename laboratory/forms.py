from django import forms
from .models import LabTestsQualityOfCleaning, LabTests, LabTestsInputControl, Bonderit


class LabTestsInputControlForm(forms.ModelForm):

    class Meta:
        model = LabTestsInputControl
        fields = ('number_of_record', 'date', 'roll_number', 'melting_number', 'batch_number',
                  'metall_thickness_in_doc', 'metall_thickness_in_fact', 'tag_weight', 'tag_len', 'zink_adhesion',
                  'zink_strength', 'air_humidity',)


class LabTestsForm(forms.ModelForm):

    class Meta:
        model = LabTests
        fields = ('roll_number', 'ral', 'paint_man', 'dry_layer_thickness_1', 'dry_layer_thickness_2',
                  'dry_layer_thickness_3', 'dry_layer_thickness_sr', 'primer_layer_thickness_1',
                  'primer_layer_thickness_2', 'primer_layer_thickness_3', 'primer_layer_thickness_sr',
                  'reverse_layer_thickness_1', 'reverse_layer_thickness_2', 'reverse_layer_thickness_3',
                  'reverse_layer_thickness_sr', 'brilliance_1', 'brilliance_2', 'brilliance_3', 'brilliance_sr',
                  'notched_adhesion_1', 'notched_adhesion_2', 'notched_adhesion_3', 'notched_adhesion_sr',
                  'resistance_to_shock_1', 'resistance_to_shock_2', 'resistance_to_shock_3', 'resistance_to_shock_sr',
                  'abrasion_resistance_1', 'abrasion_resistance_2', 'abrasion_resistance_3', 'abrasion_resistance_sr',
                  'flexural_strength', 'pencil_hardness_1', 'pencil_hardness_2', 'pencil_hardness_3',
                  'pencil_hardness_sr', 'eriksen_1', 'eriksen_2', 'eriksen_3', 'eriksen_sr', 'color_standart_1',
                  'color_standart_2', 'color_standart_3', 'color_standart_sr', 'total_thickness', 'mass_finished',
                  'len_finished', 'name_of_assistant', 'comment')


class LabTestsQualityOfCleaningForm(forms.ModelForm):

    class Meta:
        model = LabTestsQualityOfCleaning
        fields = ('number_of_record', 'free_alkalinity', 'total_alkalinity', 'pollution_coeff',)


class BonderitForm(forms.ModelForm):

    class Meta:
        model = Bonderit
        fields = ('number_of_record', 'alkali_in_ml', 'concentration')