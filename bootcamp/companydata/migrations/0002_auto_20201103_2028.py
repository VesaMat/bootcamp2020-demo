# Generated by Django 3.1.3 on 2020-11-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companydata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='postcode',
            field=models.CharField(max_length=255),
        ),
    ]
