from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Main page</h1>')

def index_my_app(request):
    return HttpResponse('<h1>My app page</h1>')
def about(request):
    return HttpResponse('<h1>About my site</h1>')

def login(request):
    return HttpResponse('<h1>Page login</h1>')

def contact(request):
    return HttpResponse('<h1>Contacts</h1>')

def add_form(request):
    return HttpResponse('<h1>Add new form</h1>')