from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



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
    if request.method == 'POST':
        if 'delete_property' in request.POST:
            property_id = request.POST['delete_property']
            property_to_delete = get_object_or_404(Properties, id=property_id, user_props=request.user)
            property_to_delete.delete()
            return redirect('userpage')
        else:
            user = request.user
            try:
                account = Account.objects.get(user = user.id)
                places = Properties.objects.filter(user_props = account)
            except Account.DoesNotExist:
                account = None
                places = None
            context = {'account': account, 'places': places, 'user': user}
            return render(request, 'userpage.html', context)
    else:
        user = request.user
        try:
            account = Account.objects.get(user = user.id)
            places = Properties.objects.filter(user_props = account)
        except Account.DoesNotExist:
            account = None
            places = None
        context = {'account': account, 'places': places, 'user': user}
        return render(request, 'userpage.html', context)

@login_required(login_url='login')
def add_property(request):
    form = AddProperty(initial={'user_props': request.user})
    if request.method == 'POST':
        form = AddProperty(request.POST)
        form.user_props = request.user
        form.price = request.POST.get('price')
        form.address = request.POST.get('address')
        form.city = request.POST.get('city')
        form.zip_code = request.POST.get('zip_code')
        form.size = request.POST.get('size')
        form.available = request.POST.get('available')
        form.save()
        return redirect('home')
    else:
        context = {'form': form}
        return render(request, 'add_property.html', context)
