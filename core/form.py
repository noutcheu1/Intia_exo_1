from django.forms import  ModelForm
from .models import Client, Personnel, Activity, Assurance


class ClientForm(ModelForm):
    class Meta:
        model = Client


class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel


class ActivityForm(ModelForm):
    class Meta:
        model = Activity


class AssuranceForm(ModelForm):
    class Meta:
        model = Assurance
