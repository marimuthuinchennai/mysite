#from django.conf.urls import url,include
from django.urls import path
from . import views
from .views import ArticleListView,ContactView,EmpUpdateView
urlpatterns = [
    #path('', views.index,name='index'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ContactView.as_view(), name='create-list'),
    path('update/', EmpUpdateView.as_view(), name='update-list'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted'),
    path('page1/', views.page1,name='index'),
    path('page2/', views.page2,name='index'),
    path('post_new/', views.post_new,name='posted')
]
