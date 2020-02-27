from django.db import models
from django.conf import settings

class History(models.Model):
    input1 = models.FloatField(blank=True,null=True)
    input2 = models.FloatField(blank=True,null=True)
    result = models.FloatField(blank=True,null=True)
    operator = models.TextField(blank=True,null=True)
    