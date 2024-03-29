
from django.contrib import admin
from django.urls import path

from bitly.views import index, create, goto, update, delete
urlpatterns = [
    path('admin/', admin.site.urls,),
    path('home/',index,name="index"),
    path('add/', create,name="create"),
    path('<str:xyz>/', goto,name="redirect"),
    path('edit/<int:pk>/', update,name="update"),
    path('delete/<int:pk>/',delete,name="delete")
]
