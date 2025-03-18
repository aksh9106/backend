# trips/models.py
from django.db import models

class Trip(models.Model):
    current_location = models.CharField(max_length=200)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    current_cycle_hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip from {self.current_location} to {self.dropoff_location}"

class LogEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"Log Entry for Trip {self.trip.id}"