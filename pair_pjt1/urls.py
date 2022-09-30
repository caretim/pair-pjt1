from django.urls import path
from . import views


app_name = "pair"

urlpatterns= [
    path("",views.index, name= "index"),
    path("create",views.create, name= "create"),
    path('send',views.send, name='send'),
]