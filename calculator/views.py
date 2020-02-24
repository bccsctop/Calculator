from django.shortcuts import render
from .models import input_form


def index(request):
    if request.method == 'POST':
        input_form

    return render(request, 'calculator/index.html')
