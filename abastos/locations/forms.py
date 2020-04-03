from django import forms
from .import models

class CreateLocation(forms.ModelForm):
    class Meta:
        model=models.Location
        fields=['name','north_coordinate','east_coordinate']
