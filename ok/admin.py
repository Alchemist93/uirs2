from django.contrib import admin
from ok.models import Citizen, Employee, Category, Position

# Register your models here.
admin.register(Citizen)(admin.ModelAdmin)
admin.register(Employee)(admin.ModelAdmin)
admin.register(Category)(admin.ModelAdmin)
admin.register(Position)(admin.ModelAdmin)
