#forms.py file is used to include Vaidation codes of different fields of admin interface & called on by '.is_valid()' method
from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):#super class 'forms.ModelForm' is important but name SignUpForm is by convention
    class Meta:
        model = SignUp
        fields = ['email','full_name']
    def clean_email(self):#function is used for validation purpose
        #the function name must start with 'clean' followed by the field name to be validated
        #write validation code here....
        email_id = self.cleaned_data.get('email') #cleaned_data gives a dictionary containing keys 'email' and 'full_name' of which we choose value correspnding to email
        email_base, provider = email_id.split('@')
        domain, extension = provider.split('.')
        if not extension == 'com':
            raise forms.ValidationError("plz enter a valid edu mail id.")
        return email_id

    def clean_full_name(self):#function used for validation purpose....
        #the function name must start with 'clean' followed by the field name to be validated
        #write validation code here...
        inst_full_name = self.cleaned_data.get('full_name')
        return inst_full_name

class ContactForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField()
    message = forms.CharField(required = False)#required = False makes the field optional to use
