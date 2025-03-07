from django.db import models


class HospitalModel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name