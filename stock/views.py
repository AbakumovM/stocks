from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import cut

menu = [{'title': 'russia', 'url_name': 'country'},
        {'title': 'china', 'url_name': 'country'},
        {'title': 'usa', 'url_name': 'country'},
        ]


def index(request):
    data = {'menu': menu}
    return render(request, 'stock/index.html', data)


def shares_in_country(request, name_country):
    return render(request, 'stock/share.html', {'menu': menu})


def test(request):
    return render(request, 'stock/test.html')

def stocks_id(request, stock_id):
    return HttpResponse(f'Hello! Stock ID: {stock_id}')


def post_details(request):
    if request.GET:
        dict_get = request.GET
        print(dict_get)
        return HttpResponse('|'.join([f'{key}={value}' for key, value in dict_get.items()]))
    return HttpResponse('GET is empty')


def login(request):
    return HttpResponse('login')


def posts_list(request, year):
    if year > 2023 or year < 1990:
        raise Http404()
    return HttpResponse(f'posts: {year}')
