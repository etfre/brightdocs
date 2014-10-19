from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from ui.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import auth

def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'login.html', {
        'form': form,
    })

@login_required
def home(request):
    return render(request, 'home.html')

def new_blueprint(request):
    c = {
    'submission': 'ye',
    }
    c.update(csrf(request))
    return render_to_response("new_blueprint.html", c)

def registration_page(request):
    form = RegisterForm()
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    return render(request, 'register.html', {
        'form': form,
    })

def register(request):
    sub_username = request.POST.get('email', '')
    sub_password = request.POST.get('password', '')
    sub_email = sub_username
    try:
        u = User.objects.get(username=sub_username)
    except:
        user = User.objects.create_user(sub_username, sub_email, sub_password)
        return redirect(home)
    c = {
    'submission': 'no',
    }
    c.update(csrf(request))
    return redirect(registration_page)

def login(request):
    username = request.POST.get('email', '')
    password = request.POST.get('password', '')
    print(username, password)
    user = auth.authenticate(username=username, password=password)
    print(user)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return redirect(home)
        else:
            print("The password is valid, but the account has been disabled!")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        print("The username and password were incorrect.")
        return redirect(request.META.get('HTTP_REFERER'))

def logout_view(request):
    auth.logout(request)
    return redirect(default_view)

def default_view(request):
    if request.user.is_authenticated():
        return redirect(home)
    return render(request, 'default.html')
