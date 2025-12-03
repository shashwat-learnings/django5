from django import forms
from django.core import validators

# custom validator
def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Email should start from s')

class Registration(forms.Form):
    first_name  = forms.CharField(max_length=70,validators=[validators.MaxLengthValidator(limit_value=64)])
    email = forms.EmailField(max_length=255,validators=[start_with_s ])
    city = forms.CharField(max_length=70)
    roll = forms.IntegerField()
    state = forms.CharField(max_length=70)

    # field by field validation
    # def clean_first_name(self):
    #     # self.cleaned_data['name'] or
    #     name_value = self.cleaned_data.get('first_name')
    #     if len(name_value) < 4:
    #         raise forms.ValidationError('Name should be more than 4 character')
    #     return name_value


    # all field in single validation
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('first_name')
        email = cleaned_data.get('email')

        if name_value and len(name_value) < 4:
            self.add_error('first_name','Enter more than or equal to 4 characters')

        if email and len(email) < 10:
            self.add_error('email','Enter email more than or equal to 10 characters')

        return cleaned_data
