from court import postnotification
from django.shortcuts import render

# Create your views here.
def postnotification(request):
    return render(request,"postnotifc.html")
