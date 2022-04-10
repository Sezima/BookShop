from django.http import HttpResponse
from django.shortcuts import render

def order(reqquest):
    return HttpResponse('hello this is order')