from datetime import date
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Grandeur

class GrandeurForm(ModelForm):
    class Meta:
        model = Grandeur
        fields = '__all__'
