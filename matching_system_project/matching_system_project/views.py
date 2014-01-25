from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Projects System</h1>' +
                        '<a href="/projects">View Projects</a>')

def projects(request):
    return HttpResponse("PROJECTS IN YOUR FACE MOFO")
