from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import myProjects,Votes, Users
from django.contrib.auth import authenticate,login,logout,login

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    myprojects=myProjects.objects.all()
    context={"projects":myprojects}
    return render(request,'index.html', context)

def register(request):
    if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            user_e=Users.objects.filter(username=username).count()
            ema_ex=Users.objects.filter(email=email).count()

            if user_e>0:
                messages.add_message(request, messages.INFO, 'username taken.')
                return redirect(register) 

            elif ema_ex>0:
                messages.add_message(request, messages.INFO, 'email registered.')
                return redirect(register)       
            else:
                if password!=confirm_password:
                    messages.add_message(request, messages.INFO, 'Passwords do not match.')
                    return redirect(register) 
                else:
                    user = Users(username=username, email=email, password=make_password(password))
                    user.save()

                    user = Users.objects.get(username=username)
                    messages.add_message(request, messages.SUCCESS, 'saved')
                    return redirect(loggin) 
        
    else:
        return render(request, "register.html")


def loggin(request):
     if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email, password=password)

        if user is not None:
            login(request,user )
            messages.add_message(request, messages.INFO, 'Successfully logged in!')
            return redirect(index)
 
        else:
            messages.add_message(request, messages.INFO, 'Invalid credentials!')
            return redirect(loggin)

     else:
        return render(request, "login.html")


def loggout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successfully!')
    return redirect(index)



# new project
def addproject(request):
    if request.method=="POST":
            image=request.FILES['landingimage']
            title = request.POST.get('title')
            
            description=request.POST.get('description')
            link=request.POST.get('link')

            project = myProjects(title=title, image=image, description=description, link=link, user=request.user)
            project.save()
            messages.add_message(request, messages.SUCCESS, 'saved')
            return redirect(index) 
        
    else:
        return render(request, "addproject.html")
# individual project

def show_project(request, id):
    project = myProjects.objects.get(id=id)
    if request.method=="POST":
            image=request.FILES['landingimage']
            title = request.POST.get('title')
            
            description=request.POST.get('description')
            link=request.POST.get('link')

            project = myProjects(title=title, image=image, description=description, link=link, user=request.user)
            project.save()
            messages.add_message(request, messages.SUCCESS, 'saved')
            return redirect(index) 
        
    else:
        return render(request, "show_project.html",{"project":project})

# profile
def profile(request):
    if request.method=="POST":
            profile=request.FILES['profile_pic']
            bio = request.POST['bio']
                       
            user = Users.objects.get(id=request.user.id)
            user.bio=bio, 
            user.profile=profile
            user.save()
            messages.add_message(request, messages.SUCCESS, 'saved')
            return render(request, "profile.html")
        
    else:
        return render(request, "profile.html")