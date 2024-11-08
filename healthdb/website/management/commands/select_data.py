from django.core.management.base import BaseCommand
from website.models import (Patients, Patient_Addresses, Patients_mobile, Doctors, 
                            Doctors_mobile, Appointments, Patient_Historical, 
                            Treatments, Bills)

class Command(BaseCommand):
    help = 'Exibe 10 registros de cada tabela no console'

    def handle(self, *args, **kwargs):
        # Seleciona 10 pacientes
        self.stdout.write("----- Patients -----")
        patients = Patients.objects.all()[:10]
        for patient in patients:
            self.stdout.write(f"{patient.patient_id} - {patient.patient_fname} {patient.patient_lname} - {patient.patient_status}")
        
        # Seleciona 10 endereços de pacientes
        self.stdout.write("\n----- Patient Addresses -----")
        addresses = Patient_Addresses.objects.all()[:10]
        for address in addresses:
            self.stdout.write(f"{address.patient_id} - {address.patient_street}, {address.patient_city}, {address.patient_state}, {address.patient_zipcode}")
        
        # Seleciona 10 números de celular de pacientes
        self.stdout.write("\n----- Patients Mobile -----")
        mobiles = Patients_mobile.objects.all()[:10]
        for mobile in mobiles:
            self.stdout.write(f"{mobile.patient_id} - {mobile.patient_mobile}")
        
        # Seleciona 10 médicos
        self.stdout.write("\n----- Doctors -----")
        doctors = Doctors.objects.all()[:10]
        for doctor in doctors:
            self.stdout.write(f"{doctor.doctor_id} - {doctor.doctor_fname} {doctor.doctor_lname} - {doctor.doctor_specialization}")
        
        # Seleciona 10 números de celular de médicos
        self.stdout.write("\n----- Doctors Mobile -----")
        doctors_mobiles = Doctors_mobile.objects.all()[:10]
        for doctor_mobile in doctors_mobiles:
            self.stdout.write(f"{doctor_mobile.doctor_id} - {doctor_mobile.doctors_mobile}")
        
        # Seleciona 10 consultas
        self.stdout.write("\n----- Appointments -----")
        appointments = Appointments.objects.all()[:10]
        for appointment in appointments:
            self.stdout.write(f"{appointment.appointment_id} - {appointment.patient_id} - {appointment.doctor_id} - {appointment.appointment_date} - {appointment.appointment_description}")
        
        # Seleciona 10 históricos de pacientes
        self.stdout.write("\n----- Patient Historical -----")
        historical = Patient_Historical.objects.all()[:10]
        for hist in historical:
            self.stdout.write(f"{hist.historical_id} - {hist.patient_id} - {hist.historical_date} - {hist.historical_describe}")
        
        # Seleciona 10 tratamentos
        self.stdout.write("\n----- Treatments -----")
        treatments = Treatments.objects.all()[:10]
        for treatment in treatments:
            self.stdout.write(f"{treatment.treatment_id} - {treatment.treatment_name} - {treatment.patient_id} - {treatment.doctor_id}")
        
        # Seleciona 10 faturas
        self.stdout.write("\n----- Bills -----")
        bills = Bills.objects.all()[:10]
        for bill in bills:
            self.stdout.write(f"{bill.bill_id} - {bill.bill_title} - {bill.patient_id} - {bill.bill_init_date} - {bill.bill_end_date}")
