# Third-party imports
import django_filters
# imports from app
from .models import SampleInformation


class SampleInformationFilter(django_filters.FilterSet):
    class Meta:
        model = SampleInformation
        fields = {'d_number': ['icontains'],
                  'worksheet_number': ['worksheet_number']}
