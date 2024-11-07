# Generated by Django 5.1.3 on 2024-11-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_patients_table'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='patients',
            constraint=models.CheckConstraint(condition=models.Q(('patient_status__in', ['Pending', 'Cancelled', 'Completed'])), name='check_patient_status'),
        ),
    ]
