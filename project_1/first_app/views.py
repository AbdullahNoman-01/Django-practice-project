from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(reponse):
   return HttpResponse("This is first_app/courses page")

def about(reponse):
   return HttpResponse("This is first_app/about page.")

def home(reponse):
   return HttpResponse("This is first_app/home page.")