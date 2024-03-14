from django.db import models
from django.contrib.auth import get_user_model

class Address(models.Model):
    street = models.CharField(max_length=100, null=False, blank=False)
    betweenStreet = models.CharField(max_length=100, null=False, blank=False)
    colony = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=5, null=True, blank=False)
    number = models.CharField(max_length=5, null=True, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)

class Patient(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=30, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False)
    ocupation = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=10, null=True, blank=False)
    email = models.EmailField(max_length=150, null=True, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    reason_consult = models.CharField(max_length=200, null=True, blank=False)
    comment = models.CharField(max_length=1000, null=True, blank=False)

class Doctor(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    professionalID = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    university = models.CharField(max_length=150, null=False, blank=False)
    speciality = models.CharField(max_length=150, null=True, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=False)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False, blank=False)
    appointment_date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    status = models.CharField(max_length=30, null=False, blank=False)
    scheduled = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    coment = models.CharField(max_length=500, null=True, blank=False)

class Service(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    cost = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=8)
    category = models.CharField(max_length=150, null=False, blank=False)

class AppoinmentService(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)

class Payment(models.Model):
    appoinment_service = models.ForeignKey(AppoinmentService, on_delete=models.CASCADE)
    subtotal = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=8)
    discount = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=8)
    bonus = models.DecimalField(null=True, blank=False, decimal_places=2, max_digits=8)
    total = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=8)
    date = models.DateField(null=False, blank=False, auto_now_add=True)
    pyment_ype = models.CharField(max_length=100, null=False, blank=False)
