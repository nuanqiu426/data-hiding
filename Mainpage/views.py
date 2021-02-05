from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from login.models import User


def You_know_me(request):
    return render(request, 'Mainpage/Found_me.html')


def login_success(request):
    name = request.POST.get("user")
    pwd = request.POST.get("password")
    message1 = '不存在此用户'
    message2 = '密码错误'
    isc = False
    user = ''
    for u in User.objects.all():
        if u.uname == name:
            user = u
            isc = True
    if user == '':
        for m in User.objects.all():
            if m.uid == name:
                user = m
                isc=True
                name=m.uname

    if user == '':

        return render(request, 'login/test3.html',{"mess":message1})
    elif isc:
        if user.upassword == pwd:
            return render(request, 'Mainpage/l_success.html',{"username":name})
        else:

            return render(request, 'login/test3.html',{"mess":message2})