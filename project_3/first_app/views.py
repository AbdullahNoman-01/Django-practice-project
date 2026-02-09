from django.shortcuts import render
# Create your views here.
def home(request):
   d = {'author' : 'Tanvir','age' : 21,'courses' : [
         {
            'id' : 1,
            'name' : "python",
            'fee' : 5000
         },
         {
            'id' : 2,
            'name' : "django",
            'fee' : 10000
         },
         {
            'id' : 3,
            'name' : "cpp",
            'fee' : 8000
         },
      ]}
   return render(request,"first_app/index.html",d)