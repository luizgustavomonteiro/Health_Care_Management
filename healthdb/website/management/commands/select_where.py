from django.core.management.base import BaseCommand
from django.db.models import Q, Count, Avg, Sum
from datetime import date
from website.models import (
    Patients, Doctors, Appointments,
    Patient_Addresses, Treatments, Bills, Doctors_mobile
)

class Command(BaseCommand):
    help = 'Perform queries on the specified models'

    def handle(self, *args, **kwargs):

        print("Query 0")
        print("*********************************************************************************")

        # 0. Total number of patients
        total_patients_count = Patients.objects.count()
        self.stdout.write(self.style.SUCCESS(f"Total Patients: {total_patients_count}"))


        print("Query 1")
        print("*********************************************************************************")

        # 1. Count of status completed patients
        completed_patients_count = Patients.objects.filter(patient_status='Completed').count()
        self.stdout.write(self.style.SUCCESS(f"Completed Status Patients Treatment: {completed_patients_count}"))

        print("Query - 2")
        print("*********************************************************************************")

        # 2. Count of doctors by specialization
        doctors_by_specialization = Doctors.objects.values('doctor_specialization').annotate(doctor_count=Count('doctor_id'))

        self.stdout.write(self.style.SUCCESS("Doctors by Specialization:"))
        for specialization in doctors_by_specialization:
            self.stdout.write(self.style.SUCCESS(f"{specialization['doctor_specialization']}: {specialization['doctor_count']} doctors"))

        print("Query - 3")
        print("*********************************************************************************")


        # 3. Count of all treatment descriptions
        treatment_descriptions_count = Treatments.objects.values('treatment_description').distinct().count()
        self.stdout.write(self.style.SUCCESS(f"Distinct Treatment Descriptions: {treatment_descriptions_count}"))


        print("Query - 4")
        print("*********************************************************************************")

        # 4. Count of addresses in New York
        addresses_in_ny_count = Patient_Addresses.objects.filter(patient_city='Texas').count()
        self.stdout.write(self.style.SUCCESS(f"Addresses in New York: {addresses_in_ny_count}"))

        print("Query - 5")
        print("*********************************************************************************")


        # 5. Count of treatments by a specific doctor (e.g., doctor with ID 2)
        treatments_for_doctor_50 = Treatments.objects.filter(doctor_id=50).count()
        self.stdout.write(self.style.SUCCESS(f"Treatments for Doctor 2: {treatments_for_doctor_50}"))
        
        print("Query - 6")
        print("*********************************************************************************")

        # 6. Count of bills generated in 2024
        bills_in_2024 = Bills.objects.filter(
            bill_init_date__year=2024
        ).count()
        self.stdout.write(self.style.SUCCESS(f"Total Bills generated in 2024: {bills_in_2024}"))

        print("Query - 7")
        print("*********************************************************************************")

        # 7. Count of appointments per doctor
        appointments_per_doctor = Appointments.objects.values(
            'doctor_id__doctor_fname', 'doctor_id__doctor_lname'
        ).annotate(appointment_count=Count('appointment_id'))

        self.stdout.write(self.style.SUCCESS("Appointments per Doctor:"))
        for doctor in appointments_per_doctor:
            self.stdout.write(self.style.SUCCESS(f"{doctor['doctor_id__doctor_fname']} {doctor['doctor_id__doctor_lname']}: {doctor['appointment_count']} appointments"))
        
        print("Query - 8")
        print("*********************************************************************************")

        # 8. Count of patients per doctor
        patients_per_doctor = Appointments.objects.values(
            'doctor_id__doctor_fname', 'doctor_id__doctor_lname'
        ).annotate(patient_count=Count('patient_id', distinct=True))

        self.stdout.write(self.style.SUCCESS("Patients per Doctor:"))
        for doctor in patients_per_doctor:
            self.stdout.write(self.style.SUCCESS(f"{doctor['doctor_id__doctor_fname']} {doctor['doctor_id__doctor_lname']}: {doctor['patient_count']} patients"))
        print("Query - 9")
        print("*********************************************************************************")

        # 9. Count of patients with more than one address
        patients_with_multiple_addresses = Patient_Addresses.objects.values(
            'patient_id'
        ).annotate(address_count=Count('address_id')).filter(address_count__gt=1).count()
        self.stdout.write(self.style.SUCCESS(f"Patients with Multiple Addresses: {patients_with_multiple_addresses}"))

        print("Query - 10")
        print("*********************************************************************************")

        # 10. Count of mobile numbers per doctor
        doctor_mobile_counts = Doctors_mobile.objects.values(
            'doctor_id__doctor_fname', 'doctor_id__doctor_lname'
        ).annotate(mobile_count=Count('doctors_mobile'))

        self.stdout.write(self.style.SUCCESS("Mobile Numbers per Doctor:"))
        for doctor in doctor_mobile_counts:
            self.stdout.write(self.style.SUCCESS(f"{doctor['doctor_id__doctor_fname']} {doctor['doctor_id__doctor_lname']}: {doctor['mobile_count']} mobile numbers"))
