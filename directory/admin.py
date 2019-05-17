from django.contrib import admin
from directory.models import Ral, PaintMan, SteelMan

# Register your models here.
admin.register(Ral)(admin.ModelAdmin)
admin.register(PaintMan)(admin.ModelAdmin)
admin.register(SteelMan)(admin.ModelAdmin)