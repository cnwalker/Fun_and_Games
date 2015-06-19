from django.conf import settings
from forms import UserProfileForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from chapters.models import Chapter

@login_required
def user_profile(request):
    args = {}
    args['successful'] = True
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/discussions/')
        else:
            args['successful'] = False
            
    else:
        user = request.user
        form = UserProfileForm()

    args.update(csrf(request))
    args['form'] = form
    args['thumbnail'] = request.user.thumbnail
    args['first_name'] = request.user.first_name
    args['last_name'] = request.user.last_name
    args['email'] = request.user.email
    args['chapter'] = request.user.chapter
    args['favorite_topics'] = request.user.favorite_topics
    args['curTitle'] = (request.user.first_name + ' ' + request.user.last_name)
    args['chapter_list'] = Chapter.objects.all()
    args['MEDIA_URL'] = settings.MEDIA_URL
    return render_to_response('user_temps/profile.html', args)
