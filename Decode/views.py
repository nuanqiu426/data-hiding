from django.shortcuts import render
from . import photo_decode
# Create your views here.

def new_decode(request):
    if request.method == 'GET':
        info='no'
        context={
            "info":info,
        }
        return render(request, 'Decode/Decode_page.html', context)
    else:
        info = 'yes'
        password = request.POST.get("pass")
        if(password==''):
            password='666'
        img_in=request.FILES.get('image_encode')
        final_info=''
        if (('.png' in str(img_in)) | ('.bmp' in str(img_in))):
            photo = request.FILES['image_encode']
            final_info=photo_decode.ps_decode(photo,password)
            final_info=final_info[0:1000]
            final_sig=photo_decode.ps_sif(photo)
            if(final_sig==''):
                final_sig='未知作者'
        context = {
            "article":final_info,
            "img":img_in,
            "sig":final_sig,
            "info": info,

        }
        return render(request, 'Decode/Decode_page.html', context)