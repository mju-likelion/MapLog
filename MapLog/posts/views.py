import requests
from django.shortcuts import render


def post_page(request):
    return render(request, "posts/post.html")
