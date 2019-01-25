from django.shortcuts import render

from django.http import HttpResponse

def index_django(request):
    	return HttpResponse("Django says Hello")
