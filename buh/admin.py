from django.contrib import admin
from buh.models import Counterparty, Interactions, Items, ItemInStorage

# Register your models here.

admin.register(Counterparty)(admin.ModelAdmin)
admin.register(Interactions)(admin.ModelAdmin)
admin.register(Items)(admin.ModelAdmin)
admin.register(ItemInStorage)(admin.ModelAdmin)
