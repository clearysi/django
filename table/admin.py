# Core django imports
from django.contrib import admin

# Third-party imports
from ajax_select.admin import AjaxSelectAdmin

# imports from app
from .models import SampleInformation, UploadFile

# Register your models here.

admin.site.register(SampleInformation)
admin.site.register(UploadFile)


class SampleInformation(AjaxSelectAdmin):
    form = SampleInformation
