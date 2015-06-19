from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib import auth
from userprofiles.models import UserProfileManager
from forms import MyRegistrationForm
from chapters.models import Chapter
import datetime

def login(request):
    args = {}
    args.update(csrf(request))
    args['curTitle'] = "Dialectic Login"
    return render_to_response('user_temps/login.html', args)

def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email = email,
                             password = password)
    if user != None: 
        auth.login(request, user)
        return HttpResponseRedirect('/discussions')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def invalid_login(request):
    return render_to_response('user_temps/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('user_temps/logout.html')

def register_user(request):
    args = {}
    args['successful'] = True
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile')
        else:
            args['successful'] = False
    args.update(csrf(request))
    args['chapter_list'] = Chapter.objects.all()
    args['form'] = MyRegistrationForm()
    return render_to_response('user_temps/register.html', args)

def register_success(request):
    return render_to_response('user_temps/register_success.html')
    
   
