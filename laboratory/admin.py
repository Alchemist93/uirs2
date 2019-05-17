from django.contrib import admin
from laboratory.models import LabTestsInputControl, LabTests, LabTestsQualityOfCleaning, Bonderit

# Register your models here.
admin.register(LabTestsInputControl)(admin.ModelAdmin)
admin.register(LabTests)(admin.ModelAdmin)
admin.register(LabTestsQualityOfCleaning)(admin.ModelAdmin)
admin.register(Bonderit)(admin.ModelAdmin)