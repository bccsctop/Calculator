from django.db import models
from django.conf import settings
from django.db import models
from django import forms
from django.forms import ModelForm

class input_form(models.Model):
    x = models.TextField(blank=True)
    y = models.TextField(blank=True)
    result = models.TextField(blank=True)
