from django.db import models
from hospitals.models import HospitalModel
from django.utils.timezone import get_current_timezone_name

class PatientModel(models.Model):
    patient_name=models.CharField(max_length=60)
    patient_age=models.IntegerField()
    patient_medical_expenditures=models.IntegerField()
    patient_admitted_on = models.DateTimeField()
    patient_admitted=models.ForeignKey(HospitalModel, on_delete = models.CASCADE)

    def __str__(self):
        return self.patient_name