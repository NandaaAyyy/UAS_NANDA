from django.urls import path
from .import views 

urlpatterns =[
    path('', views.home, name='home' ),
    path('menu/', views.menu, name='menu'),
    path('pesanan', views.pesanan, name='pesan'),
    path('terimakasih', views.terimakasih, name='terimakasih'),
    path('vieww', views.vieww, name='vieww'),
    path('daftar_vieww', views.daftar_vieww, name='daftar_vieww'),



    

]

