from django.shortcuts import render
from django import forms

from django.http import HttpResponse

def index(request):
    return HttpResponse("fala fiote")