from django.shortcuts import render
from ok.models import Employee, Citizen, Category, Position
from django.views.generic import DetailView

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
    #print(Position.depart)
    context = {
        'nav': nav,
        'cats': category,
        'person_in_category': person_in_category,

    }
    return render(request, 'category.html', context)
