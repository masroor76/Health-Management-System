from rest_framework import serializers
from .models import HospitalModel

class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model=HospitalModel
        fields="__all__"