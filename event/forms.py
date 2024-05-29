from django import forms 
from .models import Event_Table

class Event_Form(forms.ModelForm):
    class Meta:
        model = Event_Table
        fields = '__all__'