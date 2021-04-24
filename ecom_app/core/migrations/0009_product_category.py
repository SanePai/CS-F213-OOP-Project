# Generated by Django 3.1.7 on 2021-04-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_merge_20210423_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('veg', 'Vegetables'), ('fruit', 'Fruits'), ('groc', 'Groceries')], default='1', max_length=20),
        ),
    ]
