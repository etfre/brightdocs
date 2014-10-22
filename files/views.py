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
    blueprint_num = int(request.POST.get('BlueprintNumber'))
    blueprint = request.user.blueprint_set.all()[blueprint_num - 1]
    f = request.FILES['file']
    doc = blueprint.document_set.create(blueprint=blueprint,
                                        name=f.name,
                                        extension=f.name,
                                        doc_file=f)
    return redirect(request.META.get('HTTP_REFERER'))