from forms import SignupForm
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from webapp.models import *
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
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = SignupForm()
    return render_to_response(template, {'form':form},context_instance=RequestContext(request))

def redfin(request,template):
    if request.method == 'POST':        
        return render_to_response('Confirmation.html', context_instance=RequestContext(request))
    else:
        return render_to_response('Identity.html', context_instance=RequestContext(request))

def verify(request):

    # For now, we just create a new profile on every new query.
    # TODO: Create scoring system for same profile (% of matching fields?)
    profile = Profile.objects.create()
    profile.save()

    # Add all the fields that exist in our database
    for field_name, field_val in request.POST.iteritems():

        try:
            field = Field.objects.get(name=field_name)

        except Field.MultipleObjectsReturned:
            continue

        except Field.DoesNotExist:
            continue

        field_value = FieldValue.objects.create(
            field=field,
            profile=profile,
            value=field_val
        )

        field_value.save()

    return HttpResponse('Added')

def companyprofile(request, id):
    t=get_template("companyprofile.html")
    profiles=[]
    for profile in Profile.objects.all():
        first_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='first_name', profile=profile.id)))
        last_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='last_name', profile=profile.id)))
        sex_offender=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='sex_offender', profile=profile.id)))
        profiles.append((first_name, last_name, "Failed" if sex_offender else "Passed", '/api/person/id='+str(profile.id)))
    c=Context({"profiles":profiles})
    html=t.render(c)
    return HttpResponse(html)

def profile(request, id):
     t=get_template("profile.html")
     profile=Profile.objects.get(pk=id)
     sex_offender=getFirstValue(FieldValue.objects.filter(field__name='sex_offender', profile=profile.id))
     first_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='first_name', profile=profile.id)))
     last_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='last_name', profile=profile.id)))
     address=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='address', profile=profile.id)))
     crime= cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='sex_offense', profile=profile.id)))
     c=Context({"sex_offender":sex_offender, "first_name":first_name, "last_name":last_name, "address":address, "crime":crime})
     html=t.render(c)
     return HttpResponse(html)


def cleanCaps(dirtystring):
    result=""
    for word in dirtystring.split(" "):
        result+=word.capitalize()+" " 
    return result 

def getFirstValue(fieldvalueobjs):
    if len(fieldvalueobjs)==0: 
        return  "N/A"
    return fieldvalueobjs[0].value    
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

