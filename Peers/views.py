from django.shortcuts import render, get_object_or_404
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
        person = PeerIDs.objects
        return render(request, 'index.html', {'person' : person})
    return render(request, 'index.html') 

def detail(request, person_id):
    person_detail = get_object_or_404(PeerIDs, pk=person_id)
    return render(request, 'detail.html',{'person':person_detail})

def change(request):
    person = PeerIDs()
    if person.attend == True:
        person.attend = False
    else:
        person.attend = True
    person.save()
    return redirect('/peer/'+str(person.id))
