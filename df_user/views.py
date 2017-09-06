from django.shortcuts import render, redirect
from django.http import JsonResponse
from df_user.models import *
from hashlib import sha1


# Create your views here.
def register(request):
    context = {
        "title": "注册"
    }
    return render(request, 'df_user/register.html', context)


def register_exist(request):
    uname = request.GET.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    list = UserInfo.objects.all().values('uname')

    if upwd != ucpwd or {'uname': uname} in list:
        return redirect('/user/register/')
    else:
        s1 = sha1()
        s1.update(upwd.encode())
        upwd1 = s1.hexdigest()
        user = UserInfo()
        user.uname = uname
        user.upwd = upwd1
        user.uemail = uemail
        user.save()
        return render(request, 'df_user/login.html')


def login(request):
    name = request.COOKIES.get('uname')
    context = {
        "title": "登陆",
        'uname': name,
        'error_name': 0,
        'error_pwd': 0,
    }
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get("uname")
    upwd = post.get("upwd")
    s1 = sha1()
    s1.update(upwd.encode())
    upwd1 = s1.hexdigest()
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        context = {
            "title": "登陆",
            'uname': uname,
            'error_name': 1,
            'error_pwd': 0,
        }
        return render(request, 'df_user/login.html', context)
    else:
        if upwd1 == users[0].upwd:  # 登陆成功
            return render(request, 'df_user/user_center_info.html')
        else:
            context = {
                "title": "登陆",
                'uname': uname,
                'error_name': 0,
                'error_pwd': 1,
            }
            return render(request, 'df_user/login.html', context)
