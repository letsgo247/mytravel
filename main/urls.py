from django.conf.urls import url
from django.urls import path
# from django.contrib import admin
from . import views

# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import StaticViewSitemap


app_name = 'main'

# sitemaps = {
#     'static': StaticViewSitemap,
# }

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url('result', views.result, name = 'result'),
    # url('result/<int:identifier>/', views.load_result, name = 'load_result'),
    path('result', views.result, name = 'result'),
    path('result/<identifier>', views.load_result, name = 'load_result'),
    # url(r'^generate.+$', views.generate, name = 'generate'),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]