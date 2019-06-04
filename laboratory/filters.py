import django_filters
from .models import LabTests
from dal import autocomplete


#devname_url = 'roll-auto'


class TestsFilter(django_filters.FilterSet):
    #roll_number = django_filters.CharFilter(widget=autocomplete.ListSelect2(url='roll-auto'))


    class Meta:
        model = LabTests
        fields = ['roll_number']


