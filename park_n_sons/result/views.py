from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from search.forms import SearchForm
from .forms import SortForm
from django.db.models import Q
from functools import reduce
import operator
from .models import Result
from django.core.cache import cache

def result(request):
    buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]
    colours = ["E6194B", "3CB44B", "FFE119", "0082C8", "F58231", "911EB4", "46F0F0", "F032E6", "800000", "AA6E28"]
    if request.method == 'POST' and request.POST.get('userType', None) is not None:
        form = SearchForm(request.POST)
        sortForm = SortForm()
        if form.is_valid():
            data = form.cleaned_data

            words = data['keywords'].split(' ')
            userType = data['userType']
            free = data['free']
            buildingFilter = []
            if userType == 'bsns':
                buildingFilter=[2, 3, 4, 5, 6, 7, 8]
            elif userType == 'trst':
                buildingFilter=[3, 4, 5, 6, 7, 8]
            elif userType == 'sdnt':
                buildingFilter=[0, 1, 4, 5, 6, 7, 8]
            if free:
                price=0
            childFriendly = data['childFriendly']
            search = reduce(operator.or_, (Q(name__icontains=x) for x in words))
            results = Result.objects.filter(search, type_business__in=buildingFilter)
            if free:
                results = results.filter(price=0)
            if childFriendly:
                results = results.filter(childFriendly=childFriendly)
            results = results.order_by('name')

            paginator = Paginator(results, 10)
            page = request.GET.get('page')
            try:
                result_list = paginator.page(page)
            except PageNotAnInteger:
                result_list = paginator.page(1)
            except EmptyPage:
                result_list = paginator.page(paginator.num_pages)

            cache.set('results', results)
            cache.set('resultData', request.POST)
            cache.set('sort', 'name')

            return render(request, "result.html", {'results': result_list, 'business': buildingList, 'form': form, 'colours': colours, 'sort': sortForm})
    elif request.method == "POST" and cache.get('results'):
        results = cache.get('results')
        searchForm = SearchForm(cache.get('resultData'))
        sortForm = SortForm(request.POST)
        if sortForm.is_valid():
            data = sortForm.cleaned_data
            sortType = data['sort']
            if sortType == "asc":
                results = results.order_by('name')
                cache.set('sort', 'name')
            elif sortType == "desc":
                results = results.order_by('-name')
                cache.set('sort', '-name')
            elif sortType == "rate":
                results = results.order_by('-rating')
                cache.set('sort', '-rating')

        paginator = Paginator(results, 10)
        page = request.GET.get('page')
        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)

        return render(request, "result.html", {'results': result_list, 'business': buildingList, 'form': searchForm, 'colours': colours, 'sort': sortForm})
    elif request.method == 'GET' and cache.get('results'):
        results = cache.get('results')
        sortForm = SortForm()
        sort = cache.get('sort', 'name')
        results = results.order_by(sort)
        if sort == "name":
            sortInitial = 'asc'
        elif sort == "-name":
            sortInitial = 'desc'
        else:
            sortInitial = 'rate'
        sortForm.fields['sort'].initial = sortInitial

        paginator = Paginator(results, 10)
        page = request.GET.get('page')
        cache.set('page', page)
        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator.num_pages)
        
        searchForm = SearchForm(cache.get('resultData'))

        return render(request, "result.html", {'results': result_list, 'business': buildingList, 'form': searchForm, 'colours': colours, 'sort': sortForm})
        
    return HttpResponseRedirect('/search/')
    
def item(request, id):
    buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]
    item = Result.objects.get(id=id)
    page = cache.get('page', 1)
    return render(request, "item.html", {'item': item, 'business': buildingList, 'page': page})