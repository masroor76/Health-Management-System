from rest_framework import serializers
from .models import PatientModel

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model=PatientModel
        fields="__all__"