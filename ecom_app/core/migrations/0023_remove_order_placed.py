# Generated by Django 3.1.7 on 2021-04-24 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_order_placed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='placed',
        ),
    ]
