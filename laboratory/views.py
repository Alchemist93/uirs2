from django.shortcuts import render
from .forms import LabTestsForm

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
    context = {
        'form': form,
    }
    return render(request, 'newlabtestform.html', context)
