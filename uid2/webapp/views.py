from forms import SignupForm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from webapp.models import *
import json
import random
from django.core.mail import EmailMessage


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
    try:
        profile = list(FieldValue.objects.filter(field=Field.objects.get(name='first_name'),value=(request.POST['first_name'].upper())))[0].profile
        first_name = str(FieldValue.objects.filter(profile=profile).get(field=Field.objects.get(name='first_name')))
        last_name = str(FieldValue.objects.filter(profile=profile).get(field=Field.objects.get(name='last_name')))
        name = first_name + last_name
        print 'FOUND:'+name
    except:
        print 'NOT FOUND:'+request.POST['first_name']+' '+request.POST['last_name']        
        profile = Profile()
        profile.user_id =1
        profile.save()
        fv = FieldValue()
        fv.field = Field.objects.get(name='sex_offender')
        fv.profile = profile
        fv.value = False
        # Add all the fields that exist in our database
        for field_name, field_val in request.POST.iteritems():
            try:
                field = Field.objects.get(name=field_name)
            except Field.MultipleObjectsReturned:
                field = Field.objects.filter(name=field_name)[0]
            except Field.DoesNotExist:
                continue
            field_value = FieldValue.objects.create(
                field=field,
                profile=profile,
                value=field_val
                )
            field_value.save()
    first_name = FieldValue.objects.filter(field=Field.objects.get(name='first_name')).get(profile=profile).value
    last_name = FieldValue.objects.filter(field=Field.objects.get(name='last_name')).get(profile=profile).value
    name = first_name + ', ' +last_name
    html_content = get_template('email.html')
    text_content = get_template('email.txt')
    try:
        sex_offender = FieldValue.objects.filter(field=Field.objects.get(name='sex_offender')).get(profile=profile).value in ['true','True']
    except:
        sex_offender = False
    context = Context({'name': name,'sex_offender':sex_offender})
    html_content = html_content.render(context)
    text_content = text_content.render(context)
    subject, from_email, to = 'IDAPI: '+name+ ' '+"Failed" if sex_offender else "Passed", 'idapi.verify@gmail.com', 'jonzjia@gmail..com'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # email = EmailMessage('Hello', 'World', to=[settings.JON_EMAIL])
    # email.send()
    return render_to_response('Confirmation.html', context_instance=RequestContext(request))

def companyprofile(request, id):
    t=get_template("companyprofile.html")
    profiles=[]
    for profile in Profile.objects.all():
        first_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='first_name', profile=profile.id)))
        last_name=cleanCaps(getFirstValue(FieldValue.objects.filter(field__name='last_name', profile=profile.id)))
        try:
            sex_offender = FieldValue.objects.filter(field=Field.objects.get(name='sex_offender')).get(profile=profile).value in ['true','True']
        except:
            sex_offender = False
        profiles.append((first_name, last_name, "Failed" if sex_offender else "Passed", '/api/person/id='+str(profile.id)))
    c=Context({"profiles":profiles})
    html=t.render(c)
    return HttpResponse(html)

def profile(request, id):
     t=get_template("profile.html")
     profile=Profile.objects.get(pk=id)
     try:
         sex_offender = FieldValue.objects.filter(field=Field.objects.get(name='sex_offender')).get(profile=profile).value in ['true','True']
     except:
         sex_offender = False
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

