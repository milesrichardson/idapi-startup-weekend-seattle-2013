from forms import SignupForm
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.core.urlresolvers import reverse
import json
import random

def home(request, template='home.html'):
    if request.method == 'POST':
        data = request.POST.copy() # so we can manipulate data
        # lower case email
        email = data['email'].lower()
        print 'email: '+data['email']
        data['username'] =  email
        form = SignupForm(data)
        if form.is_valid():
            new_user = form.save()
            print 'user: ' +str(form.cleaned_data['username'])
            # new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = SignupForm()
    return render_to_response(template, {'form':form},context_instance=RequestContext(request))

def redfin(request,template):
    if request.method == 'POST':
        return render_to_response('Confirmation.html', context_instance=RequestContext(request))
    else:
        return render_to_response('Identity.html', context_instance=RequestContext(request))

    # if request.method == 'POST':
    #     data = request.POST.copy() # so we can manipulate data
    #     # lower case email
    #     email = data['email'].lower()
    #     data['username'] =  email
    #     form = SignupForm(data)
    #     print ' email:'+data['email']+', username:'+data['username']+', password:'+data['password']
    #     new_user = form.save()
    #     return HttpResponseRedirect(reverse('thanks'))
    # else:
    #     form = SignupForm()
    # return render_to_response(template, {'form':form},context_instance=RequestContext(request))

