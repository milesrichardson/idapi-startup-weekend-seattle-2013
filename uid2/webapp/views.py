from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.core.urlresolvers import reverse
import json
import random

# Create your views here.
def home(request,template):
    return render_to_response(template, context_instance=RequestContext(request))
