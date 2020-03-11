from django import forms
from django.contrib.auth.models import User
from registration.models import BirthRegistration, DeathRegistration, RegistrationCentre


class SearchForm(forms.Form):
    query = forms.CharField()





