from django import forms
from apps.mock.models import Project, Api


class FormMixin(object):

    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}


class AddProjectsFrom(forms.ModelForm, FormMixin):

    class Meta:
        model = Project
        fields = ('name', 'desc')


class AddApiForm(forms.ModelForm, FormMixin):

    project_id = forms.IntegerField()

    class Meta:
        model = Api
        exclude = ['project']
