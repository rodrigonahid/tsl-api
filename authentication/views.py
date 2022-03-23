from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Create your views here.
def register(req):

  if req.method == "POST":
    username = req.POST["username"]
    email = req.POST["email"]
    password = req.POST["password"]
    name = req.POST["name"]

    myuser = User.objects.create_user(username, email, password)
    myuser.name = name
    myuser.save()

  return JsonResponse({"req": "req"})

def login(req):
  return render(req, "authentication/login.html")

def logout(req):
  return render(req, "authentication/logout.html")