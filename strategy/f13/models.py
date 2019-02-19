from django.db import models

# Create your models here.

from django.db import models


class Holding(models.Model):

    report_date = models.DateTimeField('date published')
    security = models.CharField(max_length=250)
    position = models.FloatField(default=0)
    market_value = models.FloatField(default=0)



