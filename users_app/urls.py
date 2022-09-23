from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_details),
    path('add_user', views.add_user),
    path('delete_all', views.delete_all)
    
]
