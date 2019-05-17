from django.contrib import admin
from storage.models import Roll

# Register your models here.
admin.register(Roll)(admin.ModelAdmin)