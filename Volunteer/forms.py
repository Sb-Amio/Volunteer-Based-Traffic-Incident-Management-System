from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident  # replace with your model name
        fields = ['title', 'description', 'location', 'status', 'assigned_to', 'service_type', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Validate file size (2 MB max)
        max_size = 6 * 1024 * 1024  # 2 MB
        if image and image.size > max_size:
            raise ValidationError("The image is too large. Maximum size allowed is 6 MB.")

        # Validate file type
        valid_types = ["image/jpeg", "image/jpg", "image/png"]
        if image and image.content_type not in valid_types:
            raise ValidationError("Only .jpg, .jpeg, and .png files are allowed.")

        return image


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']