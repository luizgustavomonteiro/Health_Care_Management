
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('patients/', views.patient_list, name="patient_list"),
   path('patients/edit/<int:id>/', views.patient_edit, name="patient_edit"),
   path('patients/delete/<int:id>/', views.patient_delete, name="patient_delete"),
   path('doctors/', views.doctor_list, name="doctor_list"),
   path('doctors/edit/<int:id>/', views.doctor_edit, name="doctor_edit")
]
