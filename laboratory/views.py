from django.shortcuts import render
from .forms import LabTestsForm
from ok.models import Position

# Create your views here.

def new_lab_test(request):
    if request.method == 'POST':
        form = LabTestsForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = LabTestsForm()
        form.fields["name_of_assistant"].queryset = Position.objects.filter(depart__slug="laboratorija")
    context = {
        'form': form,
    }
    return render(request, 'lab/newlabtestform.html', context)
