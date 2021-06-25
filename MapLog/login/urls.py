from django.urls import path
from . import views as login_views

app_name = "login"

urlpatterns = [
    path("", login_views.login_page, name="login_page"),
]
