from django.shortcuts import render
from .models import Uw
# Create your views here.
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()

def judge(dictionary):
    str=''
    if (max(sid.polarity_scores(dictionary).values()) == sid.polarity_scores(dictionary)['neu']):
        str='这句话是相对平常的'

    if (max(sid.polarity_scores(dictionary).values()) == sid.polarity_scores(dictionary)['neg']):
        str='这句话是相对消极的'
    if (max(sid.polarity_scores(dictionary).values()) == sid.polarity_scores(dictionary)['pos']):
        str='这句话是相对乐观积极的'
    if (max(sid.polarity_scores(dictionary).values()) == sid.polarity_scores(dictionary)['compound']):
        str='\t这句话是复杂度较高，请查看详细数据'
    return str

def nlp_final(request):
    article = request.POST.get("article")
    n_analysis = sid.polarity_scores(article)
    color1 = 'pink'
    color2 = 'red'
    color3 = 'yellow'
    info='yes'
    bcolor1='linear-gradient(to top,#fff1eb,#ace0f9)'
    bcolor2= 'linear-gradient(to top,#929292,#686868)'
    bcolor3= 'linear-gradient(to top,#c1dfc4,#deecdd)'
    if '乐' in judge(article):
        return render(request, 'Nlp_analysis/Nlp_a.html',
                      {"art_detail": n_analysis,
                       "art": article + ":" + judge(article),
                       "color": color1,"bcolor":bcolor1,
                       "info":info,
                       })
    if '消' in judge(article):
        return render(request, 'Nlp_analysis/Nlp_a.html',
                      {"art_detail": n_analysis,
                       "art": article + ":" + judge(article),
                       "color": color2,"bcolor":bcolor2,
                       "info": info,
                       })
    if '平' in judge(article):
        return render(request, 'Nlp_analysis/Nlp_a.html',
                      {"art_detail": n_analysis,
                       "art": article + ":" + judge(article),
                       "color": color3,"bcolor":bcolor3,
                       "info": info,
                       })
    if '高' in judge(article):
        return render(request, 'Nlp_analysis/Nlp_a.html',
                      {"art_detail": n_analysis,
                       "art": article + ":" + judge(article),
                       "color": color3, "bcolor": bcolor3,
                       "info": info,
                       })


def nlp_test(request):
    return render(request, 'Nlp_analysis/Nlp_a.html')



