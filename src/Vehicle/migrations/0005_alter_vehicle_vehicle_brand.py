# Generated by Django 4.2 on 2023-06-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0004_alter_vehicle_vehicle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_brand',
            field=models.CharField(choices=[('Chevrolet', 'Chevrolet'), ('Force', 'Force'), ('Renault', 'Renault'), ('Jeep', 'Jeep'), ('Mitsubishi', 'Mitsubishi'), ('Ford', 'Ford'), ('Mercedes', 'Mercedes'), ('BMW', 'BMW'), ('Fiat', 'Fiat'), ('Audi', 'Audi'), ('Datsun', 'Datsun'), ('Mini', 'Mini'), ('Nissan', 'Nissan'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Jaguar', 'Jaguar'), ('Skoda', 'Skoda'), ('Mahindra', 'Mahindra'), ('Maruti', 'Maruti'), ('Tata', 'Tata'), ('Hindustan', 'Hindustan'), ('Toyota', 'Toyota'), ('Land', 'Land')], max_length=100),
        ),
    ]
