from django.shortcuts import render

# Create your views here.
def post_notification(request):
    return render(request,"postnotifc.html")
def view_notifications(request):
    return render(request,"view_notifications.html") 