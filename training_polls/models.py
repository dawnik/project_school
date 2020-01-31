from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User



class Language(models.Model):
    language = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    describe = models.CharField(max_length=700, default='')

    def __str__(self):
        return self.language

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class ListTrainee(models.Model):
    # id_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.name
