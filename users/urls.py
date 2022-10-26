from django.urls import path
from .views import create_user, save_user

urlpatterns = [
    path('create/', create_user, name="create_user"),
    path('save/', save_user, name="save_user"),
    
]
