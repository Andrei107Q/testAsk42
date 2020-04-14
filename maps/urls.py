from django.urls import path
from .views import startpage

urlpatterns = [
    path('maps', startpage, name='startpage'),

]