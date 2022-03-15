from django.contrib import admin
from .models import State, City, Hospital, Facility, Availability
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Hospital)
def afterHospitalsace(signal, instance, **kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability = Availability(hospital=instance, facility=facility)
        availability.save()


@receiver(post_save, sender=Facility)
def afteracilitysace(signal, instance, **kwargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availability = Availability(hospital=hospital, facility=instance)
        availability.save()


# this is how we stand to show fields in the table
# for services table
class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['title',
                    # 'oxygen_beds',
                    # 'oxygen_cylinder',
                    # 'ventilator',
                    ]

    # def oxygen_beds(self, object):
    #     return f'{object.oxygen_beds_available}/{object.oxygen_beds_totals}'
    #
    # def oxygen_cylinder(self, object):
    #     return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'
    #
    # def ventilator(self, object):
    #     return f'{object.ventilator_available}/{object.ventilator_total}'


# for hospital model
class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name', 'phone', 'address', 'city']


# for city model
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'state']


class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital', 'facility','total', 'available', 'updated_at']
    list_editable = ['total', 'available']


admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability, AvailabilityAdmin)
