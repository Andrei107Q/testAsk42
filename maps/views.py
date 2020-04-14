from django.shortcuts import render


def startpage(request):
    print(request.POST.get('test'))
    print(request.POST.get('test1'))
    return render(request, 'basemaps.html')