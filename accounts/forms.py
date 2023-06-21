from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django import forms
from accounts.models import CustomUser
from captcha.fields import CaptchaField


class LoginForm(AuthenticationForm):
    

    class Meta:
        model = CustomUser
        fields = {'username','password'}


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = {'username','password1','password2','email','image'}


class ChangePhoto(forms.ModelForm):
    # image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['image']


class CaptchaForm(forms.Form):
    captcha= CaptchaField()