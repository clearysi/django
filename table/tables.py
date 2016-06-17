# Third party imports
import django_tables2 as tables

# Imports from app
from .models import SampleInformation


class SampleTable(tables.Table):
#    d_number = tables.Column()
#    date = tables.DateColumn()
#    worksheet = tables.TemplateColumn('{{record.worksheet_number}}')
#    link = tables.TemplateColumn(
#        '<a href="file://{{record.link}}.xlsx" download>{{record.link}} </a>')
#    classification=tables.Column()
#    first_check = tables.Column()
#    second_check = tables.Column()

    class Meta:
        model=SampleInformation
        attrs = {"class": "paleblue"}
