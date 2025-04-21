from django.shortcuts import render,HttpResponse

from django.views import View
from finance.forms import RegistrationForm
# #function based view
# def home(request):
#     return HttpResponse("Hello World")

# #class based view
# class Home(View):
#     def get(self,request,*args,**kwargs):
#         return HttpResponse("<h1> Our class based component in Django</h1>")

# class Home(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"finance/index.html")        


class RegisterView(View):
    def get(self,request,*args,**kwars):
        form = RegistrationForm()
        return render(request,"finance/register.html",{'form':form})

