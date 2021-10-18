from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from authorize.models import AuthUser
from django.contrib.auth.models import User
from django.contrib import messages
import tkinter.messagebox #弹窗库
from tkinter import *
from django.contrib.auth.hashers import check_password

# Create your views here.
def showAuth(request):
    return render(request, "login.html", locals())

class UserInfo:
    islogin = False
    isVip = False
    authority = False
    username = ''
    password = ''



# def login_auth(request):
#     UserInfo.username = request.GET.get('username')
#     UserInfo.password = request.GET.get('password')
#     # return render(request,'index.html')
#     return HttpResponse("username or password is incorrect{},{}".format(username, password))

def login_site(request):
    UserInfo.username = request.GET.get('username')
    UserInfo.password = request.GET.get('password')

    request.session['username'] = UserInfo.username
    request.session['password'] = UserInfo.password

    user = auth.authenticate(username=UserInfo.username, password=UserInfo.password)  # 使用 Django 的 authenticate 方法来验证
    if user is not None:
        auth.login(request, user)
        UserInfo.islogin = True
        ans = AuthUser.objects.values('username','is_staff','first_name')
        for i in range(len(ans)):
            if ans[i]['username'] == UserInfo.username:
                UserInfo.isVip = ans[i]['is_staff']
                UserInfo.authority = ans[i]['first_name']
                request.session['authority'] = UserInfo.authority
                request.session['isVip'] = UserInfo.isVip
                break
        # messages.error(request, '登录成功')
        return render(request, 'index.html', {'username': UserInfo.username,'islogin':UserInfo.islogin,'isVip':UserInfo.isVip,'auth':UserInfo.authority})
    else:
        # messages.error(request, '用户名或密码不正确')
        # return render(request, 'login.html', {
        #     'login_err': 'Please recheck your username or password !'
        # })
        messages.error(request, '用户名或密码不正确')
        return render(request,'login.html')
    # return render(request, 'index.html')

def logout_site(request):
    UserInfo.islogin = False
    UserInfo.isVip = False
    logout(request)     # <==
    return HttpResponseRedirect('已退出登录')


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        email = request.POST.get("email", '')
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request,'注册成功！请登录')
        return render(request,'login.html')

def authToast(request):
    messages.error(request,'无权限访问')
    return render(request,'index.html')