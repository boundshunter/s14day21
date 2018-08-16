from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
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
    # 默认选中第一页
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    start = (current_page-1) * 10
    end = current_page * 10
    data = LIST[start+1:end+1]
    # 列表总数
    all_counter = len(LIST)
    # 取余设置
    total_count, div = divmod(all_counter, 10)
    # print(count, div)
    if div:  # 余数 不为0
        total_count += 1

    # 从1计数，count+1
    page_list = []
    # 显示当前页 前5页 后5页
    start_index = current_page - 5
    end_index = current_page + 5 + 1



    if total_count < 11:
        start_index = 1
        end_index = total_count+1
    else:
        if current_page <= 6:
            start_index = 1
            end_index = 11 + 1
        else:
            start_index = current_page - 5
            end_index = current_page + 5 + 1
            if (current_page + 5) > total_count:
                end_index = total_count + 1
                # 到最后，仍然显示10页
                start_index = total_count - 10
    for i in range(start_index, end_index):
        # 如果是当前页，加上active css配置
        if i == current_page:
            templ = '<a class="page active" href="/text/user_list/?p=%s">%s</a>' % (i, i)
        else:
            templ = '<a class="page" href="/text/user_list/?p=%s">%s</a>' % (i, i)
        page_list.append(templ)

    # print(page_list)
    page_str = mark_safe(" ".join(page_list))
    # page_str = mark_safe(page_str)
    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})


