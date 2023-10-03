from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('main/', views.main),
    path('profile/', views.profile),
    path('save_user/', views.save_user),
    path('check_user/', views.check_user),
]
