from django.shortcuts import render,HttpResponse

from django.views import View

#function based view
def home(request):
    return HttpResponse("Hello World")

#class based view
class Home(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("<h1> Our class based component in Django</h1>")