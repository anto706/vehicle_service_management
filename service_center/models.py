
from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.customer_name


class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_number


class Mechanic(models.Model):
    mechanic_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.mechanic_name


class ServiceBooking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.SET_NULL, null=True, blank=True)
    service_date = models.DateField()
    problem_description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.vehicle.vehicle_number} - {self.status}"
