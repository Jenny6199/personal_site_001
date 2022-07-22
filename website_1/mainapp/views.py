from django.shortcuts import render


def main(request):
    """Шаблон главной страницы"""
    content = {
        'title': 'старт',
    }
    return render(request, 'mainapp/index.html', context=content)
