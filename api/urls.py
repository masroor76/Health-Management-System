from django.urls import path , include
from . import views

urlpatterns=[
    path('',views.HomeView.as_view()),
    path('hospitals/',include('hospitals.urls')),
    path('patients/',include('patients.urls')),
]