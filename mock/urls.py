from django.urls import path
from mock import views

app_name = 'mock'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('project/', views.ProjectList.as_view(), name='project'),
    path('api/', views.ApiList.as_view(), name='api')
]
