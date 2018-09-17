from django.db import models
from django.forms import ModelForm
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(BaseModel):
    COUNTRY_CHOICES = (
        ('US', 'United States'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField()
    zip = USZipCodeField()
    country = models.CharField(max_length=100,
                               choices=COUNTRY_CHOICES,
                               )


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'zip', 'country']
