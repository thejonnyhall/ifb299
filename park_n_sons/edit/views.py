from django.shortcuts import render

def edit(request):
    loggedIn = request.session.get('logged_in', True)
    isBusinessOwner = request.session.get('business_owner', True)
    c = {'logged_in':loggedIn, 'is_business_owner':isBusinessOwner}
    return render(request, "edit.html", c)