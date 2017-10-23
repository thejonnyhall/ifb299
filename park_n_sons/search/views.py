from django.shortcuts import render

from .forms import SearchForm
from result.models import Result

def search(request):
    form = SearchForm()
    userType = request.user.groups.all()
    userInitial = "bsns"
    if userType:
        userType = userType[0]
        if userType.name == "Businessmen":
            userInitial = "bsns"
        elif userType.name == "Tourists":
            userInitial = "trst"
        elif userType.name == "Students":
            userInitial = "sdnt"
    form.fields['userType'].initial = userInitial

    context = {'form':form}
    return render(request, "search.html", context)

def mapscrape(request):
    if request.method == "POST":
        name=request.POST.get('name', None)
        location=request.POST.get('address', 'Brisbane City').split(',')
        suburb=None
        address=None
        if len(location) == 1:
            suburb=location[0]
        if len(location) == 2:
            address=location[0]
            suburb=location[1]
        if len(location) == 3:
            address=location[1]
            suburb=location[2]
        rating=request.POST.get('rating', 0.0)
        latitude=request.POST.get('latitude', 0.0)
        longitude=request.POST.get('longitude', 0.0)
        price=request.POST.get('price', 0)
        type=request.POST.get('type', 0)
        childFriendly=request.POST.get('childFriendly', True)
        if childFriendly=='false':
            childFriendly = False
        else:
            childFriendly = True
        r = Result(name=name, type_business=type, address=address, suburb=suburb, rating=rating, lat_coord=latitude, long_coord=longitude, price=price, childFriendly=childFriendly)
        r.save()
        return render(request, "index.html", {})
    else:
        return render(request, "mapdata.html", {})
