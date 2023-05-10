from django import forms
from .models import Patient


class SignUpForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('first_name','last_name','patient_email','mobile', 'password') #'__all__'
        labels = {
            'first_name':'First Name',
            'last_name':'Last_name',
            'patient_email':'Email',
            'mobile':'Mobile Number',
            'password':'Password',
        }