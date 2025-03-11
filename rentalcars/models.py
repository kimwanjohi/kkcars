from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    charges_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    # image = models.ImageField(upload_to='cars/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.name} {self.model}"

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driving_license = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    duration_hours = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name}"
