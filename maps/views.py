from django.shortcuts import render
from .models import Point


def startpage(request):
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')
    dot = ('lat:' + str(lat) + ' ' + 'lon:' + str(lon))
    if lat == None or lon == None:
        pass
    else:
        Point.objects.create(pointer=dot)
    return render(request, 'basemaps.html')


def showpoint(request):
    points = Point.objects.all()
    return render(request, 'showpoints.html', {'points': points})