from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'birth_day',  'citizenship', 'passport',  'inn', 'inps', 'registration',)

