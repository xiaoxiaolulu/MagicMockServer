from django import forms
from apps.mock.models import Project, Api
from core.base_forms import FormMixin


class AddProjectsFrom(forms.ModelForm, FormMixin):

    class Meta:
        model = Project
        fields = ('name', 'desc')


class AddApiForm(forms.ModelForm, FormMixin):

    project_id = forms.IntegerField()

    class Meta:
        model = Api
        exclude = ['project']
