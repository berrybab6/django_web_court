from django.shortcuts import render

# appeal page.
def appeal(request):
    return render(request,"appealPage.html")

# opponent page
def opponent(request):
    return render(request,"opponent_home.html")
