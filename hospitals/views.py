from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from hospitals.models import HospitalModel
from hospitals.serializers import HospitalSerializers

# Create your views here.


class ListHospital(APIView): 
    def get(self, request, format=None):
        hospitaList = HospitalModel.objects.all()
        serializer= HospitalSerializers(hospitaList , many = True) 
        return Response(serializer.data)
    

    def post(self, request, format=None): 
        serializer= HospitalSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save() 
        return Response(serializer.data)