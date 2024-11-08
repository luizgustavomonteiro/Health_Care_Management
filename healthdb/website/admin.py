from django.contrib import admin
from . models import Patients, Patient_Addresses, Patients_mobile, Patient_Historical, Doctors, Doctors_mobile, Treatments, Appointments, Bills

# Register your models here.


admin.site.register(Patients)
admin.site.register(Patient_Addresses)
admin.site.register(Patients_mobile)
admin.site.register(Doctors)
admin.site.register(Doctors_mobile)
admin.site.register(Treatments)
admin.site.register(Appointments)
admin.site.register(Patient_Historical)
admin.site.register(Bills)

