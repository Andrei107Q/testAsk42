from django.urls import path
from .views import startpage, showpoint

urlpatterns = [
    path('maps', startpage, name='startpage'),
    path('maps/points/', showpoint, name='showpoint'),
]