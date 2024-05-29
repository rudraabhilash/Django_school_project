from django.forms import ModelForm
from .models import attendance

class student_attendance_form(ModelForm):
    class Meta:
        model = attendance
        fields = ['student_id', 'entry_time', 'exit_time']