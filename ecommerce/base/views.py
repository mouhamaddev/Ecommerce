from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import MyForm
from .models import UserProfile
import secrets


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_page')

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse("User does not exist")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_page')
            else:
                return HttpResponse("Username and password do not match")
    else:
        form = MyForm()

    return render(request, 'login.html', {'form': form})


def user_register(request):

    if request.user.is_authenticated:
        return redirect('user_page')
    
    #my_model_instance = MyModel..get(id=1)
    #my_model_instance.my_field = 'new value'

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            token = secrets.token_hex(8)
            
            email = request.POST['email']
            password = request.POST['password1']
            if User.objects.filter(email=email).exists():
                return HttpResponse("User already exists")
            else:
                user = User.objects.create_user(username=token, password=password, email=email)
                user.save()
                profile = UserProfile(user=user)
                profile.save()
                user = User.objects.get(username=token)
                login(request, user)
            return redirect('user_page')
    else:
        form = MyForm()

    return render(request, 'register.html', {'form': form})


@login_required
def user_page(request):
    return render(request, 'user.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')

def password_reset(request):
    return render(request, 'password_reset.html')