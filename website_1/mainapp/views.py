from django.shortcuts import render


def main(request):
    """Шаблон главной страницы"""
    return render(request, 'mainapp/index.html')
