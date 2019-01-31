from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'birth_day', 'passport', 'registration', 'citizenship', 'inn', 'inps')

    def save(self):
        obj = super(EmployeeForm, self).save(commit=False)
        return obj.save()
