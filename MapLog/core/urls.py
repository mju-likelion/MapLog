from django.urls import path
from . import views as core_views

app_name = "core"

urlpatterns = [
    path("about-us/", core_views.about_us, name="about_us"),
]
