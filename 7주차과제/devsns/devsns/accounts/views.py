from django.shortcuts import render, redirect
from django.contrib import auth # 로그인, 로그아웃기능, 이미 있는 회원인지 확인  
from django.contrib.auth.models import User 

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password) # 이미 있는 회원인지, 있다면 user객체를 반환 없다면 None

        if user is not None:
            auth.login(request, user) # user객체로 로그인 
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
        # GET 요청이 들어오면 login form을 담고 있는 login.html을 띄워줌 
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

# 회원가입 
def signup(request):
    if request.method == "POST":
        # 처음 친 비밀번호와 두번째 친 비밀번호가 같을 경우 
        if request.POST['password'] == request.POST['repeat']:
            # 새로운 user 만들기 ! 
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 진행
            auth.login(request, new_user)
            return redirect('home')
    return render(request, 'register.html')