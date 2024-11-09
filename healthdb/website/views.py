from django.shortcuts import render, get_object_or_404, redirect
from .models import Patients, Doctors, Doctors_mobile
from .forms import PatientForm, PatientAddressForm, PatientMobileForm, DoctorMobileForm, DoctorForm
from django.forms import inlineformset_factory
from .models import Patient_Addresses, Patients_mobile


# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def doctor_list(request):
    doctors = Doctors.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_edit(request, id):
    
    doctor = get_object_or_404(Doctors, doctor_id=id)
    MobileFormSet = inlineformset_factory(Doctors, Doctors_mobile, form=DoctorMobileForm, extra=1, can_delete=True)

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        mobile_formset = MobileFormSet(request.POST, instance=doctor)

        if doctor_form.is_valid() and mobile_formset.is_valid():
            doctor_form.save()
            mobile_formset.save()
            return redirect('doctor_list')
        
    else:
        doctor_form=DoctorForm(instance=doctor)
        mobile_formset = MobileFormSet(instance=doctor)
        return render(request, 'doctor_edit.html',{
            'doctor_form': doctor_form,
            'mobile_formset': mobile_formset,})

        

    

def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_edit(request, id):
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
    return render(request, 'patient_edit.html', {
        'patient_form' : patient_form,
        'address_formset': address_formset,
        'mobile_formset': mobile_formset,
    })

def patient_delete(request, id):
    patient = get_object_or_404(Patients, patient_id=id)
    patient.delete()
    return redirect('patient_list')

