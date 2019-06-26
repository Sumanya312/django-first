
from django.contrib import admin
from django.urls import path

from bitly.views import index, create, goto, update, delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index),
    path('add/', create),
    path('<str:xyz>/', goto),
    path('edit/<int:pk>/', update),
    path('delete/<int:pk>/',delete)
]
