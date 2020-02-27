from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from calculator.views import index
from calculator.models import History


class indexTest(TestCase):

    def test_rootURL_mapping_to_views_index(self):
        found = resolve('/')
        self.assertEqual(found.func,index)

class Operationtest(TestCase):

    def test_plus_of_numbers(self):
        respone=self.client.post('/',{'input1':'50','input2':'5','plus':'1'})
        result=respone.context['result']
        self.assertEqual('55.0',result)

    def test_sub_of_numbers(self):
        respone=self.client.post('/',{'input1':'50','input2':'5','subtract':'1'})
        result=respone.context['result']
        self.assertEqual('45.0',result)

    def test_mul_of_numbers(self):
        respone=self.client.post('/',{'input1':'50','input2':'5','multiple':'1'})
        result=respone.context['result']
        self.assertEqual('250.0',result)

    def test_div_of_numbers(self):
        respone=self.client.post('/',{'input1':'50','input2':'5','divide':'1'})
        result=respone.context['result']
        self.assertEqual('10.0',result)
    
    

