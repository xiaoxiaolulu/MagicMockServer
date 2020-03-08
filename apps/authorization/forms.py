from django import forms
from core.base_forms import FormMixin


class LoginForm(forms.Form, FormMixin):

    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)
