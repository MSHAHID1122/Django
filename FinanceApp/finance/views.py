from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from finance.forms import RegistrationForm,TranscationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def post(self,request,*args,**kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("dashboard")
        else:
            print('FORM ERRORS :' ,form.errors)
            print('REQUEST POST:' ,request.POST)
            return render(request,"finance/register.html",{'form':form})

class Dashboard(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        return render(request,'finance/dashboard.html')        

class TranscationView(View):
    def get(self,request,*args,**kwargs):
        form = TranscationForm()
        return render(request,'finance/transcation_form.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = TranscationForm(request.POST)
        if form.is_valid():
            transcation = form.save(commit=False)
            transcation.user= request.user
            transcation.save(0)
            return redirect('dashboard')
        else:
            return render(request,'finance/transcation_form.html',{'form':form})
