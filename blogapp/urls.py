from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('top/', views.top, name="top"),
]