from django.shortcuts import render

from .models import Bb

def index(request):
    all_goods = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': all_goods})