from django.shortcuts import render, render_to_response
from . import settings
import os
import random

def test(request):
    return render(request, 'test.html')


def next(request):
    query = request.GET.get('query', '')

    if '가디건' in query:
        cate = '가디건'
    elif '남방' in query:
        cate = '남방'
    elif '맨투맨' in query:
        cate = '맨투맨'
    elif '반팔티' in query:
        cate = '반팔티'
    elif '트레이닝' in query:
        cate = '트레이닝복'
    else:
        cate = '특이한 옷'

    # print(os.path.join(settings.BASE_DIR, os.path.curdir))
    imgs = os.listdir("C:\\Users\\Hyuk\\PycharmProjects\\html_test\\html_test\\static\\img\\clothes/" + cate)
    idx = random.randrange(0, len(imgs))
    img_path = "C:\\Users\\Hyuk\\PycharmProjects\\html_test\\html_test\\static\\img\\clothes/" + cate + '/' + imgs[idx]
    print(img_path)
    return render_to_response('next.html', {
        'img_path': img_path,
    })
