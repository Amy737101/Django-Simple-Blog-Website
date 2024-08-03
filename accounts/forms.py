from django import forms
from . import models

class CreateAccounts(forms.ModelForm):
    class Meta:
        model=models.Accounts
        fields=['Name','Phone No',]