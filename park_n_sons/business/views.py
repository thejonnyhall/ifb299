from django.shortcuts import render

def business(request):
    return render(request, "business.html", {})
