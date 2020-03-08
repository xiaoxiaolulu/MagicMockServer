from django.shortcuts import redirect, reverse, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from apps.authorization.forms import LoginForm
from core.response import Response


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=telephone, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    if remember:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    return Response(code='10000').json
                else:
                    return Response(code='10001', msg='账号被冻结').json
            else:
                return Response(code='10001', msg='手机或者密码错误').json
        else:
            return Response(code='10001', msg=form.get_errors()).json


def logout_view(request):
    logout(request)
    return redirect(reverse('news:index'))
