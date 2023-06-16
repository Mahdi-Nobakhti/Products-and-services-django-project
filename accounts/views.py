from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm

def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    elif req.method == 'GET':
        form = LoginForm()
        return render(req, 'registration/login.html',{'form':form})
    elif req.method == 'POST':
            
            form = LoginForm(req.POST)
            password = req.POST.get('password')
            username = req.POST.get('username')
            
            if '@'in username :
                user = CostumUser.objects.get(email=username )
                name = user.username  
                user_email=authenticate(username=name,password=password)
                if user_email is not None:  
                    login(req,user_email)
                    return redirect('/')
                else:
                    messages.add_message(req,messages.ERROR,'Input data is not valid.')
                    return redirect('accounts:login')
            elif '@' not in username:
                user_name=authenticate(username=username,password=password)
                if user_name is not None:  
                    login(req,user_name)
                    return redirect('/')
                else:
                    messages.add_message(req,messages.ERROR,'Input data is not valid.')
                    return redirect('accounts:login')
            else:
                messages.add_message(req,messages.ERROR,'Input data is not valid.')
                return redirect('accounts:login')
    # else:
    #     messages.add_message(req,messages.ERROR,'Input data is not valid.')
    #     return redirect('accounts:login')


@login_required
def Logout(req):
     logout(req)
     return redirect('/')


def signup(req):
    if request.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save()  # ذخیره کاربر جدید
            login(request, user)  # ورود کاربر به سیستم
            return redirect('home')  # یا هر صفحه دیگری که بعد از ورود به آن هدایت شود
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

