from django.contrib import admin
from .models import PatientModel

# class HospitalAdmin(admin.ModelAdmin):
#     list_display = ('name','location')

class PatientAdmin(admin.ModelAdmin):
    list_display=('patient_name','patient_age','patient_medical_expenditures','patient_admitted')

admin.site.register(PatientModel , PatientAdmin)