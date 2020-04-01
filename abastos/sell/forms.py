from django import forms
from .import models

class CreateSell(forms.ModelForm):
    class Meta:
        model=models.SellPair
        fields=['product','quantity']
