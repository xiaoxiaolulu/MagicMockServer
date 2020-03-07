from django.shortcuts import render
from django.views.generic import View
from core.response import Response
from mock.forms import AddProjectsFrom
from mock.models import Project


def dispatch_request(request, path):
    return Response(code='10000', data=path).json


class Index(View):

    def get(self, request):
        project = Project.objects.all()
        context = {
            'project': project
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
        pass

    def delete(self, request):
        pass

    def patch(self, request):
        pass
