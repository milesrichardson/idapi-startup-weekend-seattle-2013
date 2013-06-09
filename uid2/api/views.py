from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from webapp.models import *
from django.http import (
	HttpResponse,
	HttpResponseRedirect,
	HttpResponseServerError,
	Http404,
	HttpResponseBadRequest
)
from django.core.urlresolvers import reverse
import json
import random

def create_person(request):
	return HttpResponse('')

def update_person(request):
	return HttpResponse('')

def get_person(request):
	return HttpResponse(request.get(''))

def list_persons(request):
	return HttpResponse('')

def list_query_types(request):
	return HttpResponse('')

def list_fields(request):
	return HttpResponse('')

def list_required_fields(request):
	return HttpResponse('')

def get_field(request):
	return HttpResponse('')

def new_query(request):
	return HttpResponse('')

def list_query_results(request):
	return HttpResponse('')

def list_query_results_by_person(request):
	return HttpResponse('')

def get_result(request):
	return HttpResponse('')



