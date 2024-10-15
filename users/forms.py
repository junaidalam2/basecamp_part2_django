from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)  # Create user instance without saving
        user.email = self.cleaned_data['email']  # Set email
        if commit:
            user.save()  # Save the user instance if commit is True
        return user
