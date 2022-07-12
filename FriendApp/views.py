from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from . models import Friend

# Create your views here.
def addFR(request):
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        years = request.POST.get('years')
        city = request.POST.get('city')
        position = request.POST.get('position')
        
        friends = Friend(name=name, age=age, years=years, city=city, position=position)
        friends.save()
        return redirect("friends")
    
    return render(request, "addFR.html")

def friends(request):
    friends = Friend.objects.all()
    context ={"friends":friends}
    return render(request, "friends.html", context)
 
 
def updateFR(request, id):
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        years = request.POST.get('years')
        city = request.POST.get('city')
        position = request.POST.get('position')
        
        friends = Friend(id=id, name=name, age=age, years=years, city=city, position=position)
        friends.save()
        return redirect("friends")
    
    update = Friend.objects.get(id=id)
    context = model_to_dict(update)
    return render(request, updateFR.html, context)   


def deleteFR(request, id):
    friends = Friend.objects.get(id=id)
    friends.delete()
    return redirect("friends")

     