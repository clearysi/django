import csv
import string
import random
try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model


def dump(qs, filename):
    """
    Takes in a Django queryset and spits out a csv file.

    Taken from: palewi.re/posts/2009/03/03/django-recipe-dump-your-queryset-out
    -as-a-csv-file/

    """
    model = qs.model
    f = open('/home/scleary/Lab_database/files/' + filename, 'w')
    writer = csv.writer(f)
    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == unicode:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)
    f.close()


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
