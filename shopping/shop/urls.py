from django.urls import path, include, re_path
from . import views

# import mptt_urls

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    #url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    path('closet/create', views.closet_create, name='closet_create'),
]