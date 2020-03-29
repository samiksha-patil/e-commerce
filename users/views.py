from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{ username }, Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

def home(request):
            
    context={
        
        'users':User.objects.all()
        }
    return render(request,'users/home.html',context)
    
