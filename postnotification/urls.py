from django.urls import path
from . import views

urlpatterns=[
path("",views.postnotification, name="Post_Notification"),
]