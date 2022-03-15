from django import template
from ..models import Availability

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'


@register.simple_tag
def get_availibilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')