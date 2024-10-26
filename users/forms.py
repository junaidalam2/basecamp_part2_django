from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-floating', 
            'placeholder': 'Email', 
            'id': 'id_email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-floating', 
            'placeholder': 'Password', 
            'id': 'id_password'
        })
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control form-floating', 'id': 'id_email', 'placeholder': 'Email'}),
        required=True
    )

    password1 = forms.CharField(
            label="New Password",
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password', 'id': 'id_password1'}),
            required=True
    )

    password2 = forms.CharField(
            label="Confirm New Password",
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'id': 'id_password2'}),
            required=True
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_first_name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_last_name', 'placeholder': 'Last Name'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(_("A user with that email already exists."))
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.label += ' *'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        print('user', user)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'permissions']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_first_name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_last_name', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-floating', 'id': 'id_email', 'placeholder': 'Email'}),
            'permissions': forms.Select(attrs={'class': 'form-control form-floating', 'id': 'id_permissions', 'placeholder': 'Permissions'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.label += ' *'


class UpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password', 'id': 'id_password1'}),
        required=False
    )

    password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'id': 'id_password2'}),
        required=False
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        # to enable floating labels in bootstrap
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_first_name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-floating', 'id': 'id_last_name', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-floating', 'id': 'id_email', 'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.label += ' *'
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')

        if password1:
            user.set_password(password1)

        if commit:
            user.save()
        return user