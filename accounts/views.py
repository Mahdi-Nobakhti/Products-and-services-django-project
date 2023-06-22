from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages
from .forms import *
from .models import CustomUser



def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == 'GET':
        captcha = CaptchaForm()
        return render(req, 'registration/login.html',{'captcha':captcha})
    elif req.method == 'POST':
            captcha = CaptchaForm(req.POST)
            if captcha.is_valid():
                password = req.POST.get('password')
                username = req.POST.get('username')
                
                if '@'in username :
                    user = CustomUser.objects.get(email=username )
                    name = user.username  
                    user_email=authenticate(username=name,password=password)
                    if user_email is not None:  
                        login(req,user_email)
                        return redirect('/')
                    else:
                        messages.add_message(req,messages.ERROR,'The input data is not valid !')
                        return redirect('accounts:login')
                elif '@' not in username:
                    user_name=authenticate(username=username,password=password)
                    if user_name is not None:  
                        login(req,user_name)
                        return redirect('/')
                    else:
                        messages.add_message(req,messages.ERROR,'The input data is not valid !')
                        return redirect('accounts:login')
                else:
                    messages.add_message(req,messages.ERROR,'The input data is not valid !')
                    return redirect('accounts:login')
            else: 
                messages.add_message(req,messages.ERROR,'The captcha is not valid !')
                return redirect('accounts:login')

@login_required
def Logout(req):
    if req.method == 'GET':
        return render(req, 'registration/logout.html')
    elif req.method == 'POST':     
        logout(req)
        return redirect('/')
     

def Signup(req):
    if req.method == 'GET':
        form = SignupForm()
        captcha = CaptchaForm()

        return render(req, 'registration/signup.html' , {'form':form,'captcha':captcha})
    elif req.method == 'POST':  
        captcha = CaptchaForm(req.POST)
        if captcha.is_valid():
            form = SignupForm(req.POST,req.FILES)
            print(form)
            if form.is_valid():
                form.save()
                username = req.POST.get('username')
                password = req.POST.get('password1')
                email = req.POST.get('email')
                image = req.POST.get('image')
                user=authenticate(username=username,password=password,email=email)
                if user is not None:  
                    login(req,user)
                    return redirect('/')
            
            else:
                messages.add_message(req,messages.ERROR,'The input data is not valid !')
                return redirect('accounts:signup')
        else:
            messages.add_message(req,messages.ERROR,'The captcha is not valid !')
            return redirect('accounts:signup')
        
@login_required
def delete(req,userid):
    if req.method == 'GET':
        return render(req, 'registration/delete_account.html')
    elif req.method == 'POST':
        user = CustomUser.objects.get(id = userid)
        user.delete()
        return render(req, 'registration/deleted_account.html')

@login_required
def change_photo(req):
    if req.method == 'GET':
        form = ChangePhoto(instance=req.user)
        return render(req, 'registration/change_photo.html',{'form':form})
    elif req.method == 'POST':
        form = ChangePhoto(req.POST, req.FILES, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('/')
      
        else:
            user = CustomUser.objects.get(id = req.user.id)
            user.image='default.jpg'
            user.save()
            return redirect("/")

def default_photo(req):
    user = req.user
    user.image = "default.jpg"
    user.save()
    return redirect("/")
