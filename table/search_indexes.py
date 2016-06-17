# Stdlib imports
import datetime

# Third party imports
from haystack import indexes

# Imports from app
from .models import SampleInformation


class SampleInformationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    d_number = indexes.CharField(model_attr='d_number')
    date = indexes.DateField(model_attr='date')
    worksheet_number = indexes.CharField(model_attr='worksheet_number')
    link = indexes.CharField(model_attr='link')

    def get_model(self):
        return SampleInformation

    def index_queryset(self, using=None):
        """ Used when the entire index for model is updated."""
        return self.get_model().objects.filter()
