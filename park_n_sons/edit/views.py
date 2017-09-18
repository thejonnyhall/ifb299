from django.shortcuts import render
from result.models import Results
from django.http import HttpResponseRedirect

from .forms import AddForm, ModifyForm

buildingList = ["College", "Library", "Industry", "Hotel", "Park", "Zoo", "Museum", "Restaurant", "Mall"]

def edit(request):
    global buildingList
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    c = {'logged_in':loggedIn, 'business_owner':isBusinessOwner, 'building_list':buildingList}

    return render(request, "edit.html", c)

def display(request, building):
    global buildingList
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    entry_list = Results.objects.filter(type_business=int(building))
    c = {
        'logged_in':loggedIn, 
        'business_owner':isBusinessOwner, 
        'building':buildingList[int(building)], 
        'entry_list':entry_list,
        'build_id':building
    }
    return render(request, "data.html", c)

def add(request, building):
    global buildingList
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    entry_list = Results.objects.filter(type_business=int(building))

    if request.method == "POST":
        form = AddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            r = Results(name=data['name'], 
                address=data['address'], 
                suburb=data['suburb'], 
                lat_coord=data['latitude'], 
                long_coord=data['longitude'], 
                type_business=int(building))
            r.save()
            return HttpResponseRedirect("/edit/"+build_id)
    else:
        form = AddForm()

    c = {
        'logged_in':loggedIn, 
        'business_owner':isBusinessOwner, 
        'building':buildingList[int(building)],
        'build_id':building,
        'form': form
    }
    return render(request, "add.html", c)

def modify(request, building, id):
    global buildingList
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    entry = Results.objects.get(id=id)

    if request.method == "POST":
        form = ModifyForm(request.POST)

        if form.is_valid():
            r = Results.objects.get(id=id)
            data = form.cleaned_data
            r.name=data['name']
            r.address=data['address']
            r.suburb=data['suburb']
            r.lat_coord=data['latitude']
            r.long_coord=data['longitude']
            r.save()
            return HttpResponseRedirect("/edit/"+building)
    else:
        data = {'name': entry.name, 'address': entry.address, 'suburb': entry.suburb, 'latitude': entry.lat_coord, 'longitude': entry.long_coord}
        form = ModifyForm(initial=data)

    c = {
        'logged_in':loggedIn, 
        'business_owner':isBusinessOwner, 
        'building':buildingList[int(building)], 
        'entry':entry,
        'build_id':building,
        'form': form
    }

    return render(request, "modify.html", c)