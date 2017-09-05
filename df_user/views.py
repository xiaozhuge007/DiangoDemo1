from django.shortcuts import render, redirect
from df_user.models import *
from hashlib import sha1


# Create your views here.
def register(request):
    context = {
        "title": "注册"
    }
    return render(request, 'df_user/register.html', context)


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
    context = {
        "title": "登陆"
    }
    return render(request, 'df_user/login.html', context)
