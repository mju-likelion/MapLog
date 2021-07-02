from django.urls import path
from . import views as core_views

app_name = "core"

urlpatterns = [
    path("", core_views.main_page, name="main_page"),
    path("about-us/", core_views.about_us, name="about_us"),
    path("support/", core_views.support, name="support"),
]
