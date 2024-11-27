from django import forms

class Register(forms.Form):
    name = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First and last name'}))
    mobile = forms.CharField(label="Mobile number", max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Mobile number'}))
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'At least 6 characters'}))