from django import forms

class MarksheetForm(forms.Form):
    STUDENT_ID_MAX_LENGTH = 20
    SESSION_CHOICES = [
        ('mid_year', 'Mid Year'),
        ('end_year', 'End Year'),
    ]

    student_id = forms.CharField(label='Student ID', max_length=STUDENT_ID_MAX_LENGTH)
    session = forms.ChoiceField(label='Session', choices=SESSION_CHOICES)
   
