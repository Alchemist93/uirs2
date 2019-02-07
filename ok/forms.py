from django import forms
from .models import Employee, Position, Category, Vacation


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'birth_day',  'citizenship', 'passport',  'inn', 'inps',
                  'registration')


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('position', 'depart', 'user', 'date', 'price')


class AddCategory(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class AddVacation(forms.ModelForm):

    class Meta:
        model = Vacation
        fields = ('user', 'start_vacation', 'end_vacation',)
