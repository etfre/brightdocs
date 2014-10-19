from django import forms
 
class RegisterForm(forms.Form):
    email = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    email = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())