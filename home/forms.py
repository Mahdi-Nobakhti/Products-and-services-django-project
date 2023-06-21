from django import forms
from .models import *


class NewsForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = News
        fields = ['email']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','subject','message']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'










