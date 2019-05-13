#importing forms
from django import forms

class SignupForm(forms.Form):
	name = forms.CharField(label='Enter your name', max_length=100)
	email = forms.EmailField(label='Enter your emil', max_length=100)