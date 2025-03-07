from django.urls import path
from . import views


urlpatterns=[
    path('',views.ListPatients.as_view())
]