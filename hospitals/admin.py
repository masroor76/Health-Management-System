from django.contrib import admin
from .models import HospitalModel

# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name','location')

admin.site.register(HospitalModel,HospitalAdmin)