from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request, 'login.html')



def logout_func(request):
    logout(request)
    return redirect('login')



def homepage(request):
    places = Properties.objects.all()
    context = {'places': places}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def userpage(request):
    user = request.user
    try:
        account = Account.objects.get(user = user.id)
        places = Properties.objects.filter(user_props = account)
    except Account.DoesNotExist:
        account = None
        places = None
    context = {'account': account, 'places': places, 'user': user}
    return render(request, 'userpage.html', context)
