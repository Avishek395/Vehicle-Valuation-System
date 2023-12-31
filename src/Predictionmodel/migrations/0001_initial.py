# Generated by Django 4.2 on 2023-07-16 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='Predictionmodel.carbrand')),
            ],
        ),
    ]


# import csv
# from django.db import migrations


# def load_data(apps, schema_editor):
#     CarBrand = apps.get_model('Predictionmodel', 'CarBrand')
#     Car = apps.get_model('Predictionmodel', 'Car')

#     with open('car_data.csv') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row
#         for row in reader:
#             brand_name = row[0]
#             car_name = row[1]
#             brand, _ = CarBrand.objects.get_or_create(brand=brand_name)
#             Car.objects.create(brand=brand, name=car_name)


# class Migration(migrations.Migration):
#     dependencies = [
#         ('Predictionmodel', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(load_data),
#     ]
