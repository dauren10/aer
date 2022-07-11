from django.db import models


class Aircraft(models.Model):
    priority = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    aircraft = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    errors_count = models.IntegerField()
    info_count = models.IntegerField()

    def __str__(self):
        return self.aircraft

