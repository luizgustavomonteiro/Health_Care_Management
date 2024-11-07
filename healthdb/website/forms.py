from django import forms
from .models import Patients, Patient_Addresses, Patients_mobile

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['patient_fname', 'patient_mname', 'patient_lname', 'patient_type_blood', 'patient_dob', 'patient_status']

class PatientAddressForm(forms.ModelForm):
    class Meta:
        model = Patient_Addresses
        fields = ['patient_zipcode', 'patient_state', 'patient_city', 'patient_street', 'patient_number_add']

class PatientMobileForm(forms.ModelForm):
    class Meta:
        model = Patients_mobile
        fields = ['patient_mobile']
