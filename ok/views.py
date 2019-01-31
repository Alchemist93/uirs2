from django.shortcuts import render
from ok.models import Employee, Citizen, Category, Position
from django.views.generic import DetailView
from .forms import EmployeeForm

# Create your views here.


def base_view(request):
    category = Category.objects.all()
    employee = Employee.objects.all()
    citizen = Citizen.objects.all()
    context = {
        'employee': employee,
        'citizen': citizen,
        "category": category,

     }
    return render(request, 'base.html', context)


def category_view(request, category_slug):

    category = Category.objects.get(slug=category_slug)
    nav = Category.objects.all()
    person_in_category = Position.objects.filter(depart=category)
    context = {
        'nav': nav,
        'cats': category,
        'person_in_category': person_in_category,

    }
    return render(request, 'category.html', context)


def personal_view(request, personal_slug):
    personal = Employee.objects.get(slug=personal_slug)
    position = Position.objects.get(user=personal)
    nav = Category.objects.all()
    context = {
        'personal': personal,
        'nav': nav,
        'position': position,
    }
    return render(request, 'employee.html', context)


def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    context = {
        'form': form,
    }
    return render(request, 'newemployee.html', context)
