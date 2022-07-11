from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request,slug):
    return HttpResponse(f'{slug} КОЛИЧЕСТВО СТАТЕЙ В ИНТЕРНЕТЕ, ГДЕ В КАЧЕСТВЕ ПРОСТОГО ПРОЕКТА НА DJANGO ПРЕДЛАГАЕТСЯ СДЕЛАТЬ ВАШ БЛОГ, С ПОДРОБНЫМИ ИНСТР. НО ЗА БЕСПЛАТНО: 1 054 564 651 220 шт. ')

