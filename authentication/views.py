from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(req):
  return render(req, "authentication/signup.html")

def login(req):
  return render(req, "authentication/login.html")

def logout(req):
  return render(req, "authentication/logout.html")