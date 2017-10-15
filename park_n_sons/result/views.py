from django.shortcuts import render
from django.http import HttpResponseRedirect
from search.forms import SearchForm
from django.db.models import Q
from functools import reduce
import operator
from .models import Results

def result(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            words = data['keywords'].split(' ')
            search = reduce(operator.or_, (Q(name__icontains=x) for x in words))
            results = Results.objects.filter(search)
            buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]
            
            return render(request, "result.html", {'results': results, 'business': buildingList})
        
    return HttpResponseRedirect('/search/')