from django.db import models
from datetime import date

# Create your models here.

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_fname = models.CharField(max_length=50)
    patient_mname = models.CharField(max_length=50)
    patient_lname = models.CharField(max_length=50)
    patient_type_blood = models.CharField(max_length=3)
    patient_dob = models.DateField()
    patient_status = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.patient_id} - {self.patient_fname} - {self.patient_lname}"
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.patient_dob.year - ((today.month, today.day) < (self.patient_dob.month, self.patient_dob.day))
        return age
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(patient_status__in=['Pending', 'Canceled', 'Completed']),
                name='check_patient_status'
            )
        ]
    
class Patient_Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    patient_zipcode = models.CharField(max_length=50, blank=True, null=True)  # Optional zipcode
    patient_state = models.CharField(max_length=50, blank=True, null=True)  # Optional state
    patient_city = models.CharField(max_length=50, blank=True, null=True)  # Optional city
    patient_street = models.CharField(max_length=100, blank=True, null=True)  # Optional street
    patient_number_add = models.CharField(max_length=50, blank=True, null=True)  # Optional address number

    def __str__(self):
        return f"{self.patient_id} - {self.patient_street}, {self.patient_city}, {self.patient_state}, {self.patient_zipcode}"

    
class Patients_mobile(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    patient_mobile = models.CharField(max_length=30, blank=True, null = True)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_mobile}"
    

class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_fname = models.CharField(max_length=50)
    doctor_mname = models.CharField(max_length=50)
    doctor_lname = models.CharField(max_length=50)
    doctor_specialization = models.CharField(max_length=100)
    doctor_availability = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.doctor_id} - {self.doctor_fname} - {self.doctor_lname} - {self.doctor_specialization}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(doctor_availability__in=['Available', 'Unavailable']),
                name ='check_doctor_availability'
                )   
        ]
    

class Doctors_mobile(models.Model):
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    doctors_mobile = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.doctor_id} - {self.doctors_mobile}"
    

class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.appointment_id} - {self.patient_id} - {self.doctor_id} - {self.appointment_date} - {self.appointment_description}"
    
class Patient_Historical(models.Model):
    historical_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    historical_date = models.DateField()  # Important for tracking when the record was created
    historical_describe = models.CharField(max_length=1000)
    historical_note = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.historical_id} - {self.patient_id} - {self.historical_date}"
    

class Treatments(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    treatment_name = models.CharField(max_length=100)
    treatment_description = models.CharField(max_length=1000)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(Appointments, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.treatment_id} - {self.treatment_name} - {self.patient_id} - {self.doctor_id}"

class Bills(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    bill_init_date = models.DateField()
    bill_end_date = models.DateField(blank=True, null=True)
    bill_title = models.CharField(max_length=50)
    bill_description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bill_id} - {self.bill_title} - {self.patient_id}"