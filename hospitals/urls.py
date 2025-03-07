from django.urls import path
from . import views


urlpatterns=[
    path('',views.ListHospital.as_view())
]