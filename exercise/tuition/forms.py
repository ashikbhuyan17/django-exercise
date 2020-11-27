from django import forms
from .models import contact

    # ______________________________ Form_______________________________________

# class contactForm(forms.Form):
#     name = forms.CharField(max_length=50,label="your Name")
#     message = forms.CharField(max_length=50,label="your message")
#     subject = forms.CharField(max_length=50,label="your subject")
   
    
    # ______________________________ ModelForm_______________________________________

    
class contactmodForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

