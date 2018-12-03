from .models import User, donationtype, donationMade
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        exclude = ()

class nonAuthUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('userName','password','created_date')


class DonationForm(forms.ModelForm):
    class Meta:
        model = donationMade
        fields =('user','donation','Amount','date','monthlyCommitment')





class DonationTypeForm(forms.ModelForm):
    class Meta:
        model = donationtype
        fields = '__all__'