from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('fun/', views.fun, name='fun'),
    path('main/', views.main, name='main'),
]
