from django.contrib.auth.models import User
from django.forms import  ModelForm
from .models import Client, Personnel, Activity, Assurance


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ClientForm(ModelForm):
    user = UserForm()
    class Meta:
        model = Client
        fields = "__all__"

class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        fields = "__all__"




class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"

class AssuranceForm(ModelForm):
    class Meta:
        model = Assurance
        fields = "__all__"
