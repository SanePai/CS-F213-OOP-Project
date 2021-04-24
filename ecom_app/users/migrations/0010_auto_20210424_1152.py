# Generated by Django 3.1.7 on 2021-04-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('CUSTOMER', 'CUSTOMER'), ('RETAILER', 'RETAILER'), ('WHOLESALER', 'WHOLESALER')], default='CUSTOMER', max_length=20),
        ),
    ]