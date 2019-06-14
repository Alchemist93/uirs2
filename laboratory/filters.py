import django_filters
from .models import LabTests
from dal import autocomplete


#devname_url = 'roll-auto'


class TestsFilter(django_filters.FilterSet):

    class Meta:
        model = LabTests
        fields = ['roll_number']


