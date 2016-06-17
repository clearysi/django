from models import SampleInformation
from django import template

register = template.Library()
 @register.inclusion_tag("sample_select.html")

def sample_select():
    sample_list=SampleInformation.objects.all()
    return {'sample_list': sample_list}