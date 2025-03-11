from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home page")

def login_user(request):
    pass

def logout_user(request):
    pass