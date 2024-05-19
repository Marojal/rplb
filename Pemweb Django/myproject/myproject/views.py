from django.shortcuts import render

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def login(request):
    template = "login.html"
    context = {
        'title': 'Login',
    }
    return render(request, template, context)

def register(request):
    template = "regular.html"
    context = {
        'title': 'Register',
    }
    return render(request, template, context)

def forgot_password(request):
    template = "lupa-sandi.html"
    context = {
        'title': 'Forgot Password',
    }
    return render(request, template, context)

def dashboard(request):
    template = "dashboard.html"
    context = {
        'title': 'Forgot Password',
    }
    return render(request, template, context)
def regular(request):
    template = "regular.html"
    context = {
        'title': 'Forgot Password',
    }
    return render(request, template, context)