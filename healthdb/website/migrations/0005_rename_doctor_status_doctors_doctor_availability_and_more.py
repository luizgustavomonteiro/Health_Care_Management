# Generated by Django 5.1.3 on 2024-11-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_bills_bill_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='doctor_status',
            new_name='doctor_availability',
        ),
        migrations.AddConstraint(
            model_name='doctors',
            constraint=models.CheckConstraint(condition=models.Q(('doctor_availability__in', ['Available', 'Unavailable'])), name='check_doctor_availability'),
        ),
    ]