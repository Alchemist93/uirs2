from django.shortcuts import render
from ok.models import Employee, Citizen, Category, Position, Vacation
from django.views.generic import DetailView
from .forms import EmployeeForm, PositionForm, AddCategory, AddVacation

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
    person_in_category = Position.objects.filter(depart=category)
    context = {
        'cats': category,
        'person_in_category': person_in_category,

    }
    return render(request, 'category.html', context)


def personal_view(request, personal_slug):
    personal = Employee.objects.get(slug=personal_slug)
    position = Position.objects.get(user=personal)
    vacation = Vacation.objects.filter(user=personal)
    context = {
        'personal': personal,
        'position': position,
        'vacation': vacation
    }
    return render(request, 'employee.html', context)


def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = EmployeeForm()
    context = {
        'form': form,
    }
    return render(request, 'newemployee.html', context)


def new_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = PositionForm()
    context = {
        'form': form,
    }
    return render(request, 'newposition.html', context)


def new_category(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = AddCategory()
    context = {
        'form': form,
    }
    return render(request, 'newcategory.html', context)


def new_vacation(request):
    if request.method == 'POST':
        form = AddVacation(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = AddVacation()
    context = {
        'form': form,
    }
    return render(request, 'newvacation.html', context)

