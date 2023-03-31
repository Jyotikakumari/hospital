from django import forms
from .models import *


class InsertForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ("Name",)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__" 