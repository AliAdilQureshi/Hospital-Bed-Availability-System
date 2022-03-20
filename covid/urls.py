from django.urls import path
from .views import home, HospitalDetailView

urlpatterns = [
    path('', home, name='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital_detail')
]