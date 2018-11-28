from .models import User, donationtype
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname','lastname','email','role', 'address','donation','phone')


class DonationForm(forms.ModelForm):
    class Meta:
        model = donationtype
        fields =('name','Amount','monthlyComitment')