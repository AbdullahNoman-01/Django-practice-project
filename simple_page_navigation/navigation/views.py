from django.shortcuts import render
from django.http import HttpResponse
from .import views
# Create your views here.

def about(request):
   return render(request,'navigation/about.html')
def contact(request):
   return render(request,'navigation/contact.html')