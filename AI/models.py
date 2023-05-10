from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.PositiveIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patient_email = models.CharField(max_length=30)
    mobile = models.IntegerField()
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)