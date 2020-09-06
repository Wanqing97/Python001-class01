from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('enter', views.enter),
    # path('test1', views.test1),
    # path('test2', views.test2),
    # path('login', views.login),
    # path('login2', views.login2)
]
