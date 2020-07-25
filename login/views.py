from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth 

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pw']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')