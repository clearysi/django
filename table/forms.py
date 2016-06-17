# Stdlib imports
from __future__ import unicode_literals

# Core django imports
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone
from django import forms

# Third-party imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from selectable.forms import AutoCompleteWidget

# Imports from app
from .models import SampleInformation, UploadFile
from .lookups import SampleInformationLookup



class SampleInputInformationForm(forms.ModelForm):
    d_number = forms.CharField(required=False)
    date = forms.DateField(widget=SelectDateWidget(years=range(1900, 3000)),
                           initial=timezone.now())
    worksheet_number = forms.CharField(required=False)
    link = forms.CharField(required=False)

    class Meta:
        model = SampleInformation
        fields = ['d_number', 'date', 'worksheet_number', 'link']


class ModifySampleInformationForm(forms.ModelForm):
    d_number = forms.CharField(required=False, )
    date = forms.DateField(required=False)
    worksheet_number = forms.CharField(required=False)
    link = forms.CharField(required=False)
    first_check = forms.CharField(required=False)

    class Meta:
        model = SampleInformation
        fields = ['d_number', 'date', 'worksheet_number', 'link',
                  'first_check', 'second_check']


CATEGORIES = (('VAR', 'variant'), ('POL', 'polymorphism'), ('ART', 'artefact'))


class FirstCheckForm(forms.Form):
    d_number = forms.CharField(required=False)
    date = forms.CharField(required=False)
    worksheet_number = forms.CharField(required=False)
    link = forms.CharField(required=False)
    classification = forms.ChoiceField(choices=CATEGORIES, required=True)
    first_check = forms.CharField(required=True)


class SecondCheckForm(forms.Form):
    error_css_class = 'error'
    d_number = forms.CharField(required=False)
    date = forms.CharField(required=False)
    worksheet_number = forms.CharField(required=False)
    link = forms.CharField(required=False)
    classification= forms.CharField(required=True)
    first_check = forms.CharField(required=True)
    second_check = forms.CharField(required=True)


class SampleQueryInformationForm(forms.Form):
    d_number = forms.CharField(required=False)
    start_date = forms.DateField(label="Start Date",
                                 widget=SelectDateWidget(years=range(
                                     1950, 3000
                                                                     )),
                                 initial=timezone.now())
    end_date = forms.DateField(label="End Date",
                               widget=SelectDateWidget(years=range(
                                   1950, 3000)),
                               initial=timezone.now())
    worksheet_number = forms.CharField(required=False, )
    link = forms.CharField(required=False, )


class SampleHelperForm(FormHelper):
    model = SampleInformation
    form_tag = False
    layout = Layout('name', ButtonHolder(Submit('submit', 'Filter',
                                                css_class='button white right'
                                                )))


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['upload']


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    sender = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
