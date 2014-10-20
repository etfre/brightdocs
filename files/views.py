from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from ui.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
import ui

@login_required
def upload_view(request):
    print(dir(request))
    return redirect(ui.views.new_blueprint)
