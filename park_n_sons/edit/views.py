from django.shortcuts import render
from result.models import Results

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
    c = {
        'logged_in':loggedIn, 
        'business_owner':isBusinessOwner, 
        'building':buildingList[int(building)],
        'build_id':building
    }
    return render(request, "add.html", c)

def modify(request, building, id):
    global buildingList
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    entry = Results.objects.get(id=id)
    c = {
        'logged_in':loggedIn, 
        'business_owner':isBusinessOwner, 
        'building':buildingList[int(building)], 
        'entry':entry,
        'build_id':building
    }
    return render(request, "modify.html", c)