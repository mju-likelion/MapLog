import requests
from django.shortcuts import render

def login_page(request):
    return render(request, "users/login.html")

def signup_page(request):
    return render(request, "users/signup.html")