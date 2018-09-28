from django import forms

class LoginForm(forms.Form):
	id = forms.CharField(label='ID')
	password = forms.CharField(label='PASSWORD')