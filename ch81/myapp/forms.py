from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your name",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    email = forms.EmailField(
        label="Your email",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )
    subject = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Subject (optional)"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Enter your message"}),
        label="Message",
    )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        # additional validation can go here
        return email