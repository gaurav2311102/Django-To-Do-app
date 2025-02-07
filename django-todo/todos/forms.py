from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2") 

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")  
        password2 = cleaned_data.get("password2") 

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
