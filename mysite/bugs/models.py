from django.db import models
from time import timezone
import time
import datetime
# Create your models here.


class Bug(models.Model):
    problem = models.CharField(max_length=30)
    bug_id = models.CharField(max_length=30)
    create_person = models.CharField(max_length=30)
    create_time = models.DateTimeField('Time created')  # auto_now_add=True
    note = models.CharField(max_length=500)

    def __unicode__(self):
        return self.problem
    def was_created_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)
    was_created_recently.admin_order_field = 'create_time'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'

class Stage(models.Model):
    bug = models.ForeignKey(Bug)
    status = models.CharField(max_length=30)
    update_person = models.CharField(max_length=30)
    update_time = models.DateTimeField('Time updeted')  # auto_now_add=True
    note = models.CharField(max_length=500)
    def __unicode__(self):
        return self.status

