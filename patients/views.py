from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from patients.models import PatientModel
from patients.serializers import PatientSerializers


# Create your views here.


class ListPatients(APIView): 
    def get(self, request, format=None):
        patientList = PatientModel.objects.all()
        serializer = PatientSerializers(patientList,many=True) 
        return Response(serializer.data)
    

    def post(self,request,format = None):
        serializer = PatientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)