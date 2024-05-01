from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Menu



def home(request):

    return render(request, 'home.html',{})



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('menu')
        else:
            messages.error(request, 'There was an error. Please try again.')
    return render(request, 'login.html', {})


def menu_list(request):
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list, }
    return render(request, 'menu.html',context)
