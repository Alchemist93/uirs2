from django.template.context_processors import request
from ok.models import Category


def menu(request):
    category_list = Category.objects.all()
    return {'category_list': category_list}