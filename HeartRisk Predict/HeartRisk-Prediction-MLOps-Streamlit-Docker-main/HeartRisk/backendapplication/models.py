from django.db import models

class UserProfile(models.Model):
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=10)
    duration = models.IntegerField()
    heart_rate = models.IntegerField()
    body_temp = models.FloatField()
