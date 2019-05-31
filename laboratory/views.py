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
    """
    Список всех доступных статей
    """

    # Нижеуказанные параметры можно также передать данному отображению через метод as_view()
    # url(r'^$', Posts.as_view(context_object_name='posts', template_name='posts.html))
    model = LabTestsModel
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = 'tests'
    # Название шаблона
    template_name = 'lab/labtestsview.html'
    # Количество объектов на 1 страницу
    paginate_by = 10

    def get_queryset(self):
        qs = LabTestsModel.objects.all().order_by('roll_number')
        #if not self.request.user.is_authenticated():
            #return qs.exclude(is_private=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] =

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


def tests_list(request):
    f = TestsFilter(request.GET, queryset=LabTestsModel.objects.all())
    return render(request, 'lab/labtestsview.html', {'filter': f})

