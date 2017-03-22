from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=45)
    date_added = models.DateTimeField(auto_now_add=True)

class Description(models.Model):
    description = models.TextField(max_length=1000, default=" ")
    course = models.OneToOneField(Course)
