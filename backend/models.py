from django.db import models

class Trip(models.Model):
    current_location = models.CharField(max_length=200)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    current_cycle_hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class LogEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # driving, on_duty, off_duty, sleeper_berth
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)