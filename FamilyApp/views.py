from ast import Not
from multiprocessing import AuthenticationError
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render, redirect, HttpResponse
from . models import Family
from django.contrib.auth.models import User

# Create your views here.
def FMmember(request):
    families = Family.objects.all()
    contextfm = {"families":families}
    return render(request, "FMmember.html", contextfm)


@login_required(login_url='/login') 
def addFM(request):
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        education = request.POST.get('education')
        city = request.POST.get('city')
        relation = request.POST.get('relation')
        
        
        family = Family(name=name, age=age, education=education, city=city, relation=relation)
        family.save()
        return redirect('/')
    
    return render(request, "addFM.html")



@login_required(login_url='/login') 
def updateFM(request, id):
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        education = request.POST.get('education')
        city = request.POST.get('city')
        relation = request.POST.get('relation')
        
        
        family = Family(id=id, name=name, age=age, education=education, city=city, relation=relation)
        family.save()
        return redirect('/')
    update = Family.objects.get(id=id)
    context = model_to_dict(update)
    return render(request, "updateFM.html", context)

@login_required(login_url='/login') 
def deleteFM(request, id):
    family = Family.objects.get(id=id)
    family.delete()
    return redirect('/')


def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        try:  
            checkuser = User.objects.get(email=email)
            
        except:
            if User.DoesNotExist:
                checkuser = None
        
        if checkuser is not None:
            messages.warning(request, "Sorry, Email is Already Exist....! ")   
            return redirect("signup")    
                
                
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.is_staff = True
        myuser.save()
        messages.success(request, " Your Account has been Created successfully....! ")
        return redirect('/')
     
    return render(request, "signup.html")  


def login(request):
    if request.method=="POST":
        email = request.POST['email']
        pass1 = request.POST['pass']
        
        try:
            user1 = User.objects.get(email = email)
            if user1 is not None:
                user = authenticate(request, username = user1, password=pass1)
                if user is not None:
                    auth_login(request, user)
                    return redirect("/")
                else:
                    messages.warning(request, "Invalid Email Address OR Password...!  ")
                    return redirect("login")
        except User.DoesNotExist:
            messages.warning(request, "Invalid Email Address OR Password...!  ")
            return redirect("login")
            
    else:
        return render(request, "login.html")       


@login_required(login_url='/login')            
def logout(request):
    auth_logout(request)
    messages.success(request, "User Logged Out successfully...!  ")
    return redirect("/")   