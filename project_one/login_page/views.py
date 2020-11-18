from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_page(request):
    form = CreateUserForm
   
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'home.html')
        else:
            messages.error(request,'username or password is incorrect')
            return redirect('login')

    return render(request, 'login2.html')

def register2(request):
    form = CreateUserForm
   
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'form': form}
    return render(request, 'register3.html', context)

# @login_required
# def home(request):
#         return render(request, 'home.html')

def log_out(request):
    logout(request)
    return redirect('login')