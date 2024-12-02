
from django.urls import path
from .views import auth_service

urlpatterns = [
    path("user_account/<str:action>",auth_service,name = "user_account"),
]
