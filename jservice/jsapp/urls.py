from django.urls import path

from .views import jview,regview,loginview,indexview

urlpatterns=[
    path('reg',regview),
    path('login', loginview),
    path('index', indexview),
    path('',jview)
]