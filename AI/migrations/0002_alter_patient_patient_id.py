# Generated by Django 4.1.7 on 2023-05-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
