from django import forms
from .models import Member
from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    address_1 = forms.CharField(label="Address 1")
    address_2 = forms.CharField(label="Address 2")
    city = forms.CharField(label="City")
    state = USStateSelect
    zip = USZipCodeField
    country = forms.ChoiceField(label="Country", choices=Member.COUNTRY_CHOICES)

    class Meta:
        model = Member
        fields = ("first_name", "last_name", "address_1", "address_2", "city", "state", "zip", "country")