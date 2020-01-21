from django.contrib import admin
from django.urls import path
from apiserver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.postArticle),
    path('', views.index),
]
