from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout

# Create your views here.
def register(request):
    if request.method=='GET':
        return render(request,'auth_app/register.html')
    else:
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        uname=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        User.objects.create_user(first_name=fn,last_name=ln,email=email,username=uname,password=password)
        return redirect('auth_app-login')

def signin(request):  
    if request.method=='GET': 
        return render(request,'auth_app/login.html')
    
    else:
        uname=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=uname,password=password)
        if user is not None:

            login(request,user)

            next_url=request.GET.get('next')
            if next_url is None:
             return redirect('index')
            else:
                return redirect(next_url)
        else:
            return redirect('auth_app-login')


def signout(request):
    logout(request)
    return redirect('auth_app-login')


