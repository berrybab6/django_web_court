from django.urls import path
from . import views

urlpatterns = [
    path("",views.opponent, name="opponent page"),
    path("appeal",views.appeal, name="appeal page")
]
