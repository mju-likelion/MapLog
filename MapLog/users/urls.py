from django.urls import path
from . import views as user_views

app_name = "users"

urlpatterns = [
    path("login/", user_views.login_page, name="login_page"),
    path("sign-up/", user_views.signup_page, name="signup_page"),
    path("test/", user_views.test_page, name="test_page"),
    # MY PAGE
    path("my-page/acc-info", user_views.info_page, name="info_page"),
    path("my-page/by-date", user_views.by_date_page, name="by_date_page"),
    path("my-page/by-mood", user_views.by_mood_page, name="by_mood_page"),
]
