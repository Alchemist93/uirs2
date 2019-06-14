from django.shortcuts import render
from laboratory.models import LabTests as LabTestsModel
from .forms import LabTestsForm, LabTestsInputControlForm
from ok.models import Position
from prodline.models import RollModified
from dal import autocomplete
from django.views.generic import ListView
from .filters import TestsFilter
# Create your views here.


class LabTests(ListView):
    model = LabTestsModel
    context_object_name = 'tests'
    template_name = 'lab/labtestsview.html'
    paginate_by = 5


    def get_queryset(self):
        qs = LabTestsModel.objects.all().order_by('roll_number')
        test_filtered_list = TestsFilter(self.request.GET, queryset=qs)
        #if not self.request.user.is_authenticated():
            #return qs.exclude(is_private=True)
        return test_filtered_list.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TestsFilter(self.request.GET, queryset=self.get_queryset())
        print(context)
        return context


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


def new_lab_test_input(request):
    if request.method == 'POST':
        form = LabTestsInputControlForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = LabTestsInputControlForm()
        #form.fields["roll_number"].queryset = RollModified.objects.filter(numbe="laboratorija")
    context = {
        'form': form,
    }
    return render(request, 'lab/newinputcontrolform.html', context)


class RollAuto(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RollModified.objects.all()
        if self.q:
            qs = qs.filter(number_of_roll__number_of_roll=self.q)
        return qs


