# Stdlib imports
from __future__ import unicode_literals

# Third-party imports
from selectable.base import ModelLookup
from selectable.registry import registry

# Imports from app
from .models import SampleInformation


class SampleInformationLookup(ModelLookup):
    model = SampleInformation
    search_fields = ('d_number__icontains', 'date__icontains',
                     'worksheet_name__icontains', 'link__icontains')

    def get_item_value(self, item):
        return item.d_number

    def get_item_label(self, item):
        return u"%s (%s)" % (item.d_number, item.get_all_details())


registry.register(SampleInformationLookup)
