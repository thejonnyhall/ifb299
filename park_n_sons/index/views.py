from django.shortcuts import render
#from django.http import HttpResponse
#<img id="backgroundImage" src="{% static "img/city.png" %}" alt="Brisbane City">

def index(request):
    return render(request, "index.html", {})
    #return HttpResponse("<h1>Home Page!</h1>");