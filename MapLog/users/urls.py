from django.urls import path
from . import views as login_views
from . import views as signup_views
from . import views as test_views

app_name = "users"

urlpatterns = [
    path("", login_views.login_page, name="login_page"),
    path("signup/", signup_views.signup_page, name="signup_page"),
    path("test/", test_views.test_page, name="test_page")
]
