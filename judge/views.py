from django.shortcuts import render

# judge role adding witness.
def add_witness(request):
    return render(request,"add_witness_page.html")

#judge home
def j_home(request):
    return render(request,"judgehome.html")

# view Judge Report    
def view_judge_report(request):
    return render(request,"viewjudgereport.html")