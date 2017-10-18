from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from search.forms import SearchForm
from django.db.models import Q
from functools import reduce
import operator
from .models import Results

def result(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data

        words = data['keywords'].split(' ')
        search = reduce(operator.or_, (Q(name__icontains=x) for x in words))
        results = Results.objects.filter(search)
        buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]

        paginator = Paginator(results, 10)
        page = request.GET.get('page')
        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)
        
        return render(request, "result.html", {'results': result_list, 'business': buildingList})
        
    return HttpResponseRedirect('/search/')