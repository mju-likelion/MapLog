from django.urls import path
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path("", post_views.post_page, name="post_page"),
]
