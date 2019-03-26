from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns = [
    # path('download.html', views.download),
    # # 首页的URL
    # path('', views.index),
    # path('login.html', views.login),
    # # 通用视图
    # # path('index/', views.ProductList.as_view()),
    # path('index/<id>.html', views.ProductList.as_view(),{'name': 'phone'}),
    # path('<int:id>.html', views.model_index),
    # path('add_book$', views.add_book, ),
    # path('show_book$', views.show_books),
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
]
