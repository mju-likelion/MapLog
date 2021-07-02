import requests
from django.shortcuts import redirect, render
from .models import User

def test_page(request):
    return render(request, "users/test.html")


def login_page(request):
    if request.method == 'GET':
        return render(request, "users/login.html")

    if request.method == 'POST':
        userid = request.POST.get('userid', '')
        userpw = request.POST.get('userpw', '')

        #ID, PW를 입력하지 않았을 경우
        if not (userid and userpw):
            return render(request, "users/login.html", {'error': '아이디와 비밀번호가 입력되지 않았습니다.',})

        users=User.objects.all() #user에 User모델의 요소들 넣기

        for user in users:
            #입력한 ID와 PW가 User모델의 id, pw와 같을 경우 다음 페이지로
            if user.user_id == userid and user.user_pw == userpw:
                return render(request, 'users/test.html')
            #입력한 ID와 PW가 올바르지 않은 경우
            if (user.user_id != userid) and (user.user_pw != userpw):
                return render(request, "users/login.html", {'error': '아이디와 비밀번호가 올바르지 않습니다.',})
                
            
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

# MY PAGE
def info_page(request):
    return render(request, "users/my_page/acc_info.html")

def by_date_page(request):
    return render(request, "users/my_page/by_date.html")
