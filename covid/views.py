from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, template_name='covid/index.html')
