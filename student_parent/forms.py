from django import forms
from .models import Student #class name in models
from .models import Parent

class formDataToTableColMap(forms.ModelForm):
    class Meta:
        model = Student #class name in models
        fields = '__all__'

class formParaentDataToTableCoMap(forms.ModelForm):        
    class Meta:
        model = Parent #class name in models
        fields = '__all__'
