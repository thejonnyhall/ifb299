from django.shortcuts import render

from .forms import SearchForm

def search(request):
    form = SearchForm()
    context = {'form':form}
    return render(request, "search.html", context)
