from django import forms 
from .models import Event_Table
#from multiupload.fields import MultiFileField

class Event_Form(forms.ModelForm):
    class Meta:
        #images = MultiFileField(min_num=1, max_num=10, max_file_size=1024 * 1024 * 5)
        model = Event_Table
        fields = '__all__'