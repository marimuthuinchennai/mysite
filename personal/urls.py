#from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted')
]
