from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )   
from captcha.fields import CaptchaField
class CaptchaForm(forms.Form):
    captcha = CaptchaField()