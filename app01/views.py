from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
# Create your views here.


def index(request, name):
    return HttpResponse(name)


def login(request):
    var = reverse('author:login')
    print(var)
    return HttpResponse(var)


def tpl1(request):
    url_list = [1, 2, 3, 4, 5]
    return render(request, 'tpl1.html', {'url_list': url_list})


def tpl2(request):
    name = 'root'

    return render(request, 'tpl2.html', {'name': name})


def tpl3(request):
    relt = '已经存在'
    return render(request, 'tpl3.html', {'relt': relt})

