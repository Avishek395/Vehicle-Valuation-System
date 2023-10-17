# Generated by Django 4.2 on 2023-07-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0005_alter_vehicle_vehicle_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Year',
            field=models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_brand',
            field=models.CharField(choices=[('Chevrolet', 'Chevrolet'), ('Force', 'Force'), ('Renault', 'Renault'), ('Jeep', 'Jeep'), ('Mitsubishi', 'Mitsubishi'), ('Ford', 'Ford'), ('Mercedes', 'Mercedes'), ('BMW', 'BMW'), ('Fiat', 'Fiat'), ('Audi', 'Audi'), ('Datsun', 'Datsun'), ('Mini', 'Mini'), ('Nissan', 'Nissan'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Jaguar', 'Jaguar'), ('Skoda', 'Skoda'), ('Mahindra', 'Mahindra'), ('Maruti', 'Maruti'), ('Tata', 'Tata'), ('Hindustan', 'Hindustan'), ('Toyota', 'Toyota'), ('Land', 'Land'), ('Suzuki', 'Suzuki')], max_length=100),
        ),
    ]