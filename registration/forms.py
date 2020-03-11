from django import forms
from django.contrib.auth.models import User
from .models import RegistrationCentre, BirthRegistration, DeathRegistration


class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationCentreForm(forms.ModelForm):
    class Meta:
        model = RegistrationCentre
        fields = ('reg_centre_name', 'reg_centre_type', 'reg_centre_county', 'reg_centre_email', 'reg_centre_location')


class BirthRegistrationForm(forms.ModelForm):
    class Meta:
        model = BirthRegistration
        fields = ('first_name', 'middle_name', 'surname', 'gender', 'date_of_birth', 'mothers_name', 'fathers_name',
                  'county', 'constituency', 'reference_number', 'id_no', 'birth_reg_centre')
        widgets = {
            'date_of_birth': DateInput(),
        }


class DeathRegistrationForm(forms.ModelForm):
    class Meta:
        model = DeathRegistration
        fields = ('date_of_death', 'current_county', 'death_reg_centre', 'current_constituency', 'cause_of_death', 'occupation', 'status',
                  'children', 'children_no')
        widgets = {
            'date_of_death': DateInput(),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
