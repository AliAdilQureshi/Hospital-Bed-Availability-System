from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=300, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Services(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, primary_key=True)
    oxygen_beds_totals = models.IntegerField(default=0)
    oxygen_beds_available = models.IntegerField(default=0)
    oxygen_cylinder_total = models.IntegerField(default=0)
    oxygen_cylinder_available = models.IntegerField(default=0)
    ventilator_total = models.IntegerField(default=0)
    ventilator_available = models.IntegerField(default=0)

    def __str__(self):
        return self.hospital.name
