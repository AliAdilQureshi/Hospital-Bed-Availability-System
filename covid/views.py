from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Facility, State, City, Hospital


def home(request):
    facilities = Facility.objects.all().order_by('pk')
    cities = City.objects.all()
    states = State.objects.all()
    hospital = Hospital.objects.all()
    context = {
        'facilities' : facilities,
        'cities' : cities,
        'states' : states,
        'hospital' : hospital
    }
    return render(request, template_name='covid/index.html', context=context)
