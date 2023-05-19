# Generated by Django 3.2.19 on 2023-05-19 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autotrader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('brand', models.CharField(choices=[('bmw', 'Bmw'), ('mercedes-benz', 'Mercedes-benz'), ('audi', 'Audi'), ('volkswagen', 'Volkswagen'), ('volvo', 'Volvo'), ('ford', 'Ford'), ('toyota', 'Toyota'), ('honda', 'Honda'), ('nissan', 'Nissan'), ('mazda', 'Mazda'), ('tesla', 'Tesla'), ('renault', 'Renault'), ('peugeot', 'Peugeot')], max_length=32)),
                ('description', models.TextField()),
                ('mileage', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('gearbox', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='automatic', max_length=32)),
                ('fueltype', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid')], default='petrol', max_length=32)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, default='../default_post_tyyyjl', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]