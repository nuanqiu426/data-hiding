from django.shortcuts import render
from .models import Img
from PIL import Image
import numpy as np
from . import uni
import datetime
from . import photo_encode
import os
# Create your views here.






def encode_processing(request):
    if request.method == 'GET':
        info = 'no'
        context = {
            "info":info,

        }
        return render(request, 'Encode/Encode_page.html',context)
    else:
        info = 'yes'
        # 加密信息
        information_initial=uni.repair(uni.encode(request.POST.get("ask")))
        password = request.POST.get("pwd")
        if(password==''):
            password='666666'
        confirm=request.POST.get("confirm")
        sig=uni.repair(uni.encode(request.POST.get("sig")))


        code_ex = bin(int(password))
        code_ex = str(code_ex).replace('0b', '').rjust(20, '0')
        information_encode=uni.encrypt(code_ex, information_initial)
        information_decode=uni.decode(uni.encrypt(code_ex, information_encode))





        tips='请确认你的信息(bmp 或者 png)'
        phototime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        img_initial = Img(img_url=request.FILES.get('image_initial'),img_info=phototime)


        img_in = img_initial.img_url
        if(('.png' in str(img_in) )| ('.bmp' in str(img_in))):
            photo = request.FILES['image_initial']
            tips_error = ''
            img_initial.save()
            photo=Image.open(photo)
            photo_new=photo_encode.ps_hide(photo,information_encode,sig,confirm)
            photoname='fixed✔_'+str(img_in).replace('img/','')
            path='media//img_encode//'
            photo_new.save(path+photoname)


        else:

            tips_error = '重新放一张Png格式的图吧，亲'
            return render(request, 'Encode/Encode_page.html', {"tips_error":tips_error})

        # image_real=Image.open(img_initial_information)
        context = {
        "inf":information_encode,
        "pas":code_ex,
        "inf2":information_decode,
        "tips":tips,
        "tips_error":tips_error,
        "imge":str(img_in),
        "phototime":phototime,
        "path":photoname,
        "confirm":confirm,
        "sig":sig,
        "info":info,



        }
        return render(request, 'Encode/Encode_page.html',context)



