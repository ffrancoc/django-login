from django.shortcuts import render, redirect

def default_view(request):
    return redirect('login')

def index_view(request):
    context = {}
    return render(request, 'index.html', context=context)

def login_view(request):
    context = {}
    return render(request, 'login.html', context=context)