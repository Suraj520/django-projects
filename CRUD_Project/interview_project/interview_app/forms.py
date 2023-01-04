from django import forms
from .models import InterviewSession
class AddUserForm(forms.ModelForm):
    class Meta:
        model = InterviewSession
        fields = ("first_name","last_name","designation")
        #adding bootstrap widgets to each class
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'})
        }