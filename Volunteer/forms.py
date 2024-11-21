from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location',  'service_type', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Check file size (e.g., max 5MB)
            if image.size > 6 * 1024 * 1024:
                raise ValidationError("The image file size should be less than 6MB.")

            # Use Pillow to check the image format
            try:
                image_file = Image.open(image)
                if image_file.format not in ["JPEG", "PNG"]:
                    raise ValidationError("Only JPEG and PNG images are allowed.")
            except (IOError, ValueError):
                raise ValidationError("Invalid image file.")

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
