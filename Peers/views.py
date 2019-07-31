from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PeerIDs


def index(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'index.html')
    else:
        persons = PeerIDs.objects
        return render(request, 'index.html', {'persons' : persons})
    return render(request, 'index.html') 