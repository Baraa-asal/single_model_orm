from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_details),
    path('add_user', views.hey)
]
