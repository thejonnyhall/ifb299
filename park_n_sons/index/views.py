from django.shortcuts import render
from django.shortcuts import redirect
#from django.http import HttpResponse
#<img id="backgroundImage" src="{% static "img/city.png" %}" alt="Brisbane City">

def index(request):
    if request.user.is_authenticated():
        return redirect('search')
    return render(request, "index.html", {})
    #return HttpResponse("<h1>Home Page!</h1>");