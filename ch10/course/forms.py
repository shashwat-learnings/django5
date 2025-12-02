from django import forms

class Registration(forms.Form):
    first_name  = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=255)
    city = forms.CharField(max_length=70)
    roll = forms.IntegerField()
    state = forms.CharField(max_length=70)