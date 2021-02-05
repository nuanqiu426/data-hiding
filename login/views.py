from django.shortcuts import render
from .models import User
from .models import Whisper
import datetime
import string
import random
# Create your views here.


def login_green(request):
    return render(request, 'login/test3.html')



def reg(request):
    if request.method == 'GET':
        return render(request, 'login/Register.html')
    else:
        idn = request.POST.get("id_number")
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        guess=request.POST.get("guess")
        tip_error1="该账号已被注册"
        tip_error2 = "没输入完整亲"
 
        if idn == '' or name == '' or pwd == '' or guess == '':
            return render(request,'login/Register.html',{"tip":tip_error2})
        for u in User.objects.all():
            if u.uid == idn:
                # context = {
                # "tip": tip_error1,
                # }
                return render(request, 'login/Register.html')
        
            
        try:
            person = User(uid=idn, uname=name, upassword=pwd,uflag=guess)
            person.save()
        except:
            context={
                "tip":tip_error1,
            }
            return render(request, 'login/Register.html',context)

        return render(request, 'login/test3.html')



def whis(request):
    if request.method == 'GET':
        info='no'
        word = ['发生甚么事了', '关于这个网站的一些意见建议?', '好久没见面了！',
                '下星期约个饭呀', '今天喝了什么奶茶', '剧荒,推荐我看？']
        word_f = random.choice(word)
        photo_url="../../static/image/look2.png"
        tip='有想要对我说的话吗'
        context = {
            "info":info,
            "word": word_f,
            "photo_url": photo_url,
            "tip":tip,
        }
        return render(request, 'login/Answer_1988.html',context)
    else:
        info ='yes'

        ask = request.POST.get("ask")
        whispertime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        alphabet=''.join(random.sample(string.ascii_letters+string.digits+string.punctuation,10))
        Whisper_info = Whisper(Now_time=whispertime, ask=ask, Num_plate=alphabet)
        Whisper_info.save()

        photo_url = "../../static/image/look3.png"
        context={
            "alphabet": alphabet,
            "info": info,
            "photo_url": photo_url,
        }
        return render(request, 'login/Answer_1988.html',context)


def ans(request):
    global isc
    if request.method == 'GET':
        info='no'
        context = {
            "info":info,
            "back": "../../static/image/fuck1.png",
        }
        return render(request, 'login/Answer_final.html',context)
    else:

        num = request.POST.get("num")
        isc1 = False
        user = ''
        for u in Whisper.objects.all():
            if u.Num_plate == num:
                answer = u.answer
                ask=u.ask
                isc1 = True
                break
        if isc1:
            if(answer==""):
                answer='老笨比还没看消息,过会再来试试呗'
                b="../../static/image/fuck1.png"
                reply = "消息提示"
            else:
                b="../../static/image/fuck2.png"
                reply = "那我的回答是"
            info = 'yes'
            context = {
                "info": info,
                "answer":answer,
                "ask":ask,
                "back": b,
                "reply": reply,
            }
            return render(request, 'login/Answer_final.html',context )
        else:
            info = 'no'
            context = {
                "info":info,
                "mess":'密钥是不是记错了',
                "back": "../../static/image/fuck1.png",

            }
            return render(request, 'login/Answer_final.html',context )








