# Generated by Django 3.2.19 on 2023-05-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_enctdp', upload_to='images/'),
        ),
    ]
