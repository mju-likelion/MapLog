import requests
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import User

def test_page(request):
    return render(request, "users/test.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['userpw']
        user = auth.authenticate(request, user_id=username, user_pw=password)
        if user is not None:
            auth.login(request, user)
            return redirect('users:test.html')
        else:
            return render(request, "users/login.html", {'error':'잘못된 입력입니다.'})
    return render(request, "users/login.html")

def signup_page(request):
    if request.method == 'GET':
        return render(request, "users/signup.html")

    if request.method == 'POST':
        user_email = request.POST.get('email', '')
        user_id = request.POST.get('myid', '')
        user_pw = request.POST.get('mypw', '')
        user_name = request.POST.get('name', '')
        user_birth = request.POST.get('birthday', '')

        if (user_email or user_id or user_pw or user_name or user_birth) == '':
            return redirect('users:signup_page') 
        else:
            user = User(
                user_email = user_email,
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name,
                user_birth = user_birth
            )
            user.save()
    return redirect('users:test_page')

    