
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('patients/', views.patient_list, name="patient_list"),
   path('patients/edit/<int:id>/', views.edit_patient, name='edit_patient'),
   path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),
]
