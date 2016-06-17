# Stdlib imports
from __future__ import unicode_literals

# Core django imports
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Third-party imports
from audit_log.models.managers import AuditLog

# Create your models here.


CATEGORIES = (('VAR', 'variant'), ('POL', 'polymorphism'), ('ART', 'artefact'))


#class TableManager(models.Manager):
#    @property
#    def with_counts(self):
#        from django.db import connection
#        cursor = connection.cursor()
#        cursor.execute("""
#            SELECT t.id, t.d_number, t.date, t.worksheet_number, t.link,
#            t.first_check COUNT(*)
#            FROM table_sampleinformation t, table_response r
#            WHERE t.id=r.table_id
#            ORDER BY t.date DESC""")
#        result_list = []
#        for row in cursor.fetchall():
#            t = self.model(id=row[0], d_number=row[1], date=row[2],
#                           worksheet_number=row[3], link=row[4],
#                           first_check=row[5])
#            t.num_reponses = row[6]
#            result_list.append(t)
#        return result_list


@python_2_unicode_compatible
class SampleInformation(models.Model):
    d_number = models.CharField(max_length=10, unique=True)
    date = models.DateField()
    worksheet_number = models.CharField(max_length=6)
    link = models.CharField(max_length=500)
    classification= models.CharField(max_length=50, choices=CATEGORIES,
                                   default="not_checked")
    first_check = models.CharField(max_length=50,
                                   default="not_checked")
    second_check = models.CharField(max_length=50, default="not_checked")
    audit_log = AuditLog()
#    objects = TableManager()

    def __str__(self):
        return self.d_number


class Response(models.Model):
    table = models.ForeignKey(SampleInformation)
    person_name = models.CharField(max_length=50)
    response = models.TextField()


@python_2_unicode_compatible
class MailRequest(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100000000)
    sender = models.EmailField(max_length=100)

    def __str__(self):
        return self.subject


class UploadFile(models.Model):
    upload = models.FileField(upload_to='/home/scleary/Lab_database/files')
