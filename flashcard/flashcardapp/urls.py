from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = '絵カードアプリ'
admin.site.site_title = '絵カード' 
admin.site.site_header = '絵カード' 
admin.site.index_title = 'メニュー'

app_name = 'flashcardapp'
urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('demotop', views.DemoTopPage.as_view(), name="demotoppage"),
    path('demomain', views.DemoMainPage.as_view(), name="demomainpage"),
    
    path('top', views.TopPage.as_view(), name='toppage'),
    path('main', views.MainPage.as_view(), name='mainpage'),
    path('add_mistaken', views.AddMistaken, name='add_mistaken'),
    path('remove_mistaken', views.RemoveMistaken, name='remove_mistaken'),
]