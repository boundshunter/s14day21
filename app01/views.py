from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from utils import pagination


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

LIST = []
for a in range(200):
    LIST.append(a)


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    # 生成对象 @property 把函数变成属性，调用不用加()
    page_obj = pagination.Page(current_page, len(LIST))
    data = LIST[page_obj.start+1:page_obj.end+1]
    page_str = page_obj.page_str('/text/user_list/')
    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})

user_info = {
    'jfsu': {'pwd': 'abc123'},
    'xhsu': {'pwd': 'aaa123'},
}


def login_1(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:  # none
            return render(request, 'login.html')

        if dic['pwd'] == p:
            res = redirect('/index/')
            res.set_cookie('username111', u, max_age=10)
            return res
        else:
            return render(request, 'login.html')


def index_1(request):
    v = request.COOKIES.get('username111')
    if not v:
        return redirect('/login/')
    else:
        return render(request, 'index.html', {'curr_user': v})


def cookie(request):
    # 设置cookie
    rep = HttpResponse("aaa")
    rep = render(request, 'index.html')
    rep.set_cookie(key, value)
    rep.set_signed_cookie(key, value, salt='加密盐')
    # 设置cookie N秒后时效  秒为单位
    rep.set_cookie('username11', 'value', max_age=10)
    # 设置cookie 截止时间生效
    import datetime
    current_date = datetime.datetime.utcnow()
    current_date = current_date + datetime.timedelta(second=5)
    rep.set_cookie('username111', 'value', expires=current_date)

    # 做一个checkbox,选中值，true，把选中值换算成时间，传入设置cookie，就可以实现多久时间免登陆

    #     参数：
    #     key,              键
    #     value='',         值
    #     max_age=None,     超时时间
    #     expires=None,     超时时间(IE requires expires, so set it if hasn't been already.)
    #     path='/',         Cookie生效的路径，/ 表示根路径，特殊的：跟路径的cookie可以被任何url的页面访问
    #     domain=None,      Cookie生效的域名
    #     secure=False,     https传输
    #     httponly=False    只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖
    #                       document.cookie 获取不到cookie

    #