from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.series_list, name='series_list'),
    path('<slug:slug>/', views.series_detail, name='series_detail'),
]
