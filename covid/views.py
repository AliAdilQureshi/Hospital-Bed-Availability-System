from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Facility, State, City, Hospital


def home(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')
    facilities = Facility.objects.all().order_by('pk')
    if selected_state_id:

        cities = City.objects.filter(state=selected_state_id)
    else:
        cities = City.objects.all()
    states = State.objects.all()
    hospitals = Hospital.objects.all()
    if selected_city_id:
        hospital = Hospital.objects.filter(city=City(pk=selected_city_id))

    context = {
        'facilities' : facilities,
        'cities' : cities,
        'states' : states,
        'hospital' : hospitals,
        'selected_state_id' : selected_state_id,
        'selected_city_id' : selected_city_id,
        'selected_facility_id' : selected_facility_id
    }
    return render(request, template_name='covid/index.html', context=context)
