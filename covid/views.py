from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Services, State, City


def home(request):
    services = Services.objects.all()
    cities = City.objects.all()
    states = State.objects.all()
    context = {
        'services' : services,
        'cities' : cities,
        'states' : states
    }
    return render(request, template_name='covid/index.html', context=context)
