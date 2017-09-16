from django.shortcuts import render, render_to_response
from . import settings
import os
import random

def test(request):
    return render(request, 'test.html')


def next(request):
    query = request.GET.get('query', '')
    # print(os.path.join(settings.BASE_DIR, os.path.curdir))
    imgs = os.listdir("C:\\Users\\Hyuk\\PycharmProjects\\html_test\\html_test\\static\\img")
    idx = random.randrange(0, len(imgs))
    img_path = imgs[idx]
    print(img_path)
    return render_to_response('next.html', {
        'img_path': img_path,
    })
