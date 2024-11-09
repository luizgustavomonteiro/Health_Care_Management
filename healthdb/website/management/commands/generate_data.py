from django.core.management.base import BaseCommand
from faker import Faker
from website.models import Patients, Patient_Addresses, Patients_mobile, Doctors, Doctors_mobile, Appointments, Patient_Historical, Treatments, Bills
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Generates fake sample data for all models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate Patients
        blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        patient_status = ["Pending", "Canceled", "Completed"]

        for _ in range(50):  # Adjust number of patients as needed
            patient = Patients.objects.create(
                patient_fname=fake.first_name(),
                patient_mname=fake.first_name(),
                patient_lname=fake.last_name(),
                patient_type_blood=random.choice(blood_types),
                patient_dob=fake.date_of_birth(minimum_age=18, maximum_age=90),
                patient_status=random.choice(patient_status)
            )
            self.stdout.write(self.style.SUCCESS(f'Patient created: {patient}'))

            # Generate Patient Address
            Patient_Addresses.objects.create(
                patient_id=patient,
                patient_zipcode=fake.zipcode(),
                patient_state=fake.state(),
                patient_city=fake.city(),
                patient_street=fake.street_address(),
                patient_number_add=fake.building_number()
            )
            self.stdout.write(self.style.SUCCESS(f'Address created for patient: {patient.patient_id}'))

            # Generate Patient Mobile
            Patients_mobile.objects.create(
                patient_id=patient,
                patient_mobile=fake.phone_number()
            )
            self.stdout.write(self.style.SUCCESS(f'Mobile number created for patient: {patient.patient_id}'))

        # Generate Doctors
        doctor_specializations = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General"]
        doctor_availability = ["Available", "Unavailable"]

        for _ in range(10):  # Adjust number of doctors as needed
            doctor = Doctors.objects.create(
                doctor_fname=fake.first_name(),
                doctor_mname=fake.first_name(),
                doctor_lname=fake.last_name(),
                doctor_specialization=random.choice(doctor_specializations),
                doctor_availability=random.choice(doctor_availability)
            )
            self.stdout.write(self.style.SUCCESS(f'Doctor created: {doctor}'))

            # Generate Doctor's Mobile
            Doctors_mobile.objects.create(
                doctor_id=doctor,
                doctors_mobile=fake.phone_number()
            )
            self.stdout.write(self.style.SUCCESS(f'Mobile number created for doctor: {doctor.doctor_id}'))

        # Generate Appointments
        for _ in range(100):  # Adjust number of appointments as needed
            patient = Patients.objects.order_by('?').first()
            doctor = Doctors.objects.order_by('?').first()
            appointment_date = fake.date_this_year()
            appointment_description = f"Routine check-up for {patient.patient_fname} {patient.patient_lname}"

            appointment = Appointments.objects.create(
                patient_id=patient,
                doctor_id=doctor,
                appointment_date=appointment_date,
                appointment_description=appointment_description
            )
            self.stdout.write(self.style.SUCCESS(f'Appointment created: {appointment}'))

        # Generate Patient Historical Records
        for _ in range(30):  # Adjust number of historical records as needed
            patient = Patients.objects.order_by('?').first()
            historical_date = fake.date_this_year()
            historical_describe = f"Historical record for {patient.patient_fname} {patient.patient_lname}"
            historical_note = "No significant changes."

            Patient_Historical.objects.create(
                patient_id=patient,
                historical_date=historical_date,
                historical_describe=historical_describe,
                historical_note=historical_note
            )
            self.stdout.write(self.style.SUCCESS(f'Historical record created for patient: {patient.patient_id}'))

        # Generate Treatments
        for _ in range(50):  # Adjust number of treatments as needed
            patient = Patients.objects.order_by('?').first()
            doctor = Doctors.objects.order_by('?').first()
            appointment = Appointments.objects.order_by('?').first()
            treatment_name = "Physical Therapy" if random.choice([True, False]) else "Surgery"
            treatment_description = f"{treatment_name} for {patient.patient_fname} {patient.patient_lname}"

            Treatments.objects.create(
                treatment_name=treatment_name,
                treatment_description=treatment_description,
                patient_id=patient,
                doctor_id=doctor,
                appointment_id=appointment
            )
            self.stdout.write(self.style.SUCCESS(f'Treatment created: {treatment_name} for patient: {patient.patient_id}'))

        # Generate Bills
        for _ in range(50):  # Adjust number of bills as needed
            patient = Patients.objects.order_by('?').first()
            bill_init_date = fake.date_this_year()
            bill_end_date = bill_init_date + timedelta(days=random.randint(1, 30))
            bill_title = "Medical Services"
            bill_description = f"Medical bill for {patient.patient_fname} {patient.patient_lname}"

            Bills.objects.create(
                patient_id=patient,
                bill_init_date=bill_init_date,
                bill_end_date=bill_end_date,
                bill_title=bill_title,
                bill_description=bill_description
            )
            self.stdout.write(self.style.SUCCESS(f'Bill created: {bill_title} for patient: {patient.patient_id}'))

        self.stdout.write(self.style.SUCCESS('Fake sample data generation complete!'))
