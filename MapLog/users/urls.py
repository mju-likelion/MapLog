from django.urls import path
from . import views as user_views

app_name = "users"

urlpatterns = [
    path("login/", user_views.login_page, name="login_page"),
    path("signup/", user_views.signup_page, name="signup_page"),
    path("test/", user_views.test_page, name="test_page"),
    # MY PAGE
    path("mypage/accinfo", user_views.info_page, name="info_page"),
]
