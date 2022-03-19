from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse


def hello_world(request):
    print(reverse('hello_world'))
    return HttpResponse('hello world!')


def hello_china(request):
    return HttpResponse('hello china!')


def hello_html(request):
    """
    响应html内容
    :param request:
    :return:
    """
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html!</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    return HttpResponse("article: {}".format(month))


def search(request):
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功!')


def test(request, num):
    if int(num) % 2 == 0:
        return HttpResponse("{}是偶数!".format(num))
    else:
        return HttpResponse("{}是奇数!".format(num))


def render_str(request):
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    return render(request, 'index.html')
