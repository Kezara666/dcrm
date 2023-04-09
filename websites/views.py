from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(user_name=user_name,password=password)
            login(request,user)
            messages.success(request,'You have successful register')
            return redirect('home')

    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request, 'register.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request,'you have Logout successful')
    return render(request, 'home.html', {})
