from django.shortcuts import render, get_object_or_404, redirect
from .models import Patients, Doctors
from .forms import PatientForm, PatientAddressForm, PatientMobileForm
from django.forms import inlineformset_factory
from .models import Patient_Addresses, Patients_mobile


# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def doctor_list(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def edit_patient(request, id):
    patient = get_object_or_404(Patients, patient_id=id)

    AddressFormSet = inlineformset_factory(Patients, Patient_Addresses, form=PatientAddressForm, extra=1, can_delete=True)
    MobileFormSet = inlineformset_factory(Patients, Patients_mobile,  form=PatientMobileForm, extra=1, can_delete=True)

    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)
        address_formset = AddressFormSet(request.POST, instance=patient)
        mobile_formset = MobileFormSet(request.POST, instance=patient)

        if patient_form.is_valid() and address_formset.is_valid() and mobile_formset.is_valid():
            patient_form.save()
            address_formset.save()
            mobile_formset.save()
            return redirect('patient_list')
        
    else:
        patient_form = PatientForm(instance=patient)
        address_formset = AddressFormSet(instance=patient)
        mobile_formset = MobileFormSet(instance=patient)
    return render(request, 'edit_patient.html', {
        'patient_form' : patient_form,
        'address_formset': address_formset,
        'mobile_formset': mobile_formset,
    })

def delete_patient(request, id):
    patient = get_object_or_404(Patients, patient_id=id)
    patient.delete()
    return redirect('patient_list')

