from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from search.forms import SearchForm
from django.db.models import Q
from functools import reduce
import operator
from .models import Results
from django.core.cache import cache

def result(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            words = data['keywords'].split(' ')
            userType = data['userType']
            buildingFilter = []
            if userType == 'bsns':
                buildingFilter=[2, 3, 4, 5, 6, 7, 8]
            elif userType == 'trst':
                buildingFilter=[3, 4, 5, 6, 7, 8]
            elif userType == 'sdnt':
                buildingFilter=[0, 1, 4, 5, 6, 7, 8]
            search = reduce(operator.or_, (Q(name__icontains=x) for x in words))
            results = Results.objects.filter(search, type_business__in=buildingFilter)

            buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]

            paginator = Paginator(results, 10)
            page = request.GET.get('page')
            try:
                result_list = paginator.page(page)
            except PageNotAnInteger:
                result_list = paginator.page(1)
            except EmptyPage:
                result_list = paginator.page(paginator.num_pages)

            searchForm = SearchForm()
            cache.set('results', results)

            return render(request, "result.html", {'results': result_list, 'business': buildingList, 'form': searchForm})
    elif request.method == 'GET' and cache.get('results'):
        results = cache.get('results')

        buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]

        paginator = Paginator(results, 10)
        page = request.GET.get('page')
        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)
        
        searchForm = SearchForm()
        return render(request, "result.html", {'results': result_list, 'business': buildingList, 'form': searchForm})
        
    return HttpResponseRedirect('/search/')