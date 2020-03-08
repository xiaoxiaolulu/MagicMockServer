from django.shortcuts import render
from django.views.generic import View
from core.response import Response
from apps.mock.forms import AddProjectsFrom, AddApiForm
from apps.mock.models import Project, Api


def dispatch_request(request, path):
    return Response(code='10000', data=path).json


class Index(View):

    def get(self, request):
        project = Project.objects.all()
        interface = Api.objects.all()
        context = {
            'projects': project,
            'interfaces': interface
        }
        return render(request, 'index.html', context=context)


class ProjectList(View):

    def post(self, request):
        form = AddProjectsFrom(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            desc = form.cleaned_data.get('desc')
            Project.objects.create(name=name, desc=desc)
            return Response(code='10000').json

        else:
            return Response(code='10001', msg=form.get_errors()).json

    def delete(self, request):
        pass

    def patch(self, request):
        pass


class ApiList(View):

    def get(self, request):
        pass

    def post(self, request):
        form = AddApiForm(request.POST)

        if form.is_valid():
            project_id = form.cleaned_data.get('project_id')
            method = form.cleaned_data.get('method')
            name = form.cleaned_data.get('name')
            url = form.cleaned_data.get('url')
            body = form.cleaned_data.get('body')

            project = Project.objects.get(pk=project_id)
            Api.objects.create(method=method, name=name, url=url, body=body, project=project)
            return Response(code='10000').json

        else:
            return Response(code='10001', msg=form.get_errors()).json

    def delete(self, request):
        pass

    def patch(self, request):
        pass
