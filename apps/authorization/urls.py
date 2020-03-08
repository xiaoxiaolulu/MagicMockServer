from django.urls import path
from apps.authorization import views

app_name = 'authorization'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout')
]
