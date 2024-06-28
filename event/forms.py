from django import forms 
from .models import Event_Table, Event_Image

class Event_Form(forms.ModelForm):
    class Meta:
        model = Event_Table
        fields = '__all__'
        
class Event_Image_Form(forms.ModelForm):
    event_image_location = forms.ImageField(label='Upload Event Image:')
    class Meta:
        model = Event_Image
        fields = ['event_image_location']                