import django_filters
from .models import LabTests


class TestsFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = LabTests
        fields = ['comment']


