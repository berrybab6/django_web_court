from django.urls import path
from . import views

urlpatterns = [
    path("post_notification",views.post_notification, name="post_notification"),
    path("view_notifications",views.view_notifications , name="view notification")

]
