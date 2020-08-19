from django.urls import path
from . import views

urlpatterns = [
    path("addwitness",views.add_witness, name="add witness"),
    path("",views.j_home, name="judge home"),
    path("judgereport",views.view_judge_report, name="view judge report")
    
]
