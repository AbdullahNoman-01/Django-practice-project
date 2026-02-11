from django.shortcuts import render,redirect
from .import models
# Create your views here.
def home(request):
   student = models.student.objects.all()
   return render(request,'first_app/home.html',{'data':student})

def delete_student(request,id):
   student = models.student.objects.get(pk=id).delete()
   return redirect("home_page")