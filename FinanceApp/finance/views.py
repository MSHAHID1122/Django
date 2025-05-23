from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from finance.forms import RegistrationForm,TranscationForm,GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TransactionModel,Goal
from django.db.models import Sum
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
        transaction = TransactionModel.objects.filter(user = request.user)
        goals = Goal.objects.filter(user = request.user)
        totalIncome = TransactionModel.objects.filter(user = request.user,Transcation_type ='Income').aggregate(Sum('amount'))['amount__sum'] or 0
        totalExpense = TransactionModel.objects.filter(user = request.user,Transcation_type ='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
        net_saving = totalIncome - totalExpense
        remaining_saving = net_saving
        goal_progress = []
        
        for goal in goals:
            if remaining_saving>=goal.amount:
                goal_progress.append({'goal':goal,'progress':100})
                remaining_saving -= goal.amount
            elif remaining_saving<goal.amount:
                per = (remaining_saving/goal.amount)*100
                goal_progress.append({'goal':goal,'progress':per}) 
                remaining_saving -= goal.amount
            else:
                goal_progress.append({'goal':goal,'progress':0})    
        context = {
        "transaction":transaction,
        'income':totalIncome,
        'expense':totalExpense,
        'total_saving':net_saving,
        'goal_progress':goal_progress
        }
        return render(request,'finance/dashboard.html',context)     

class TranscationView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form = TranscationForm()
        return render(request,'finance/transcation_form.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = TranscationForm(request.POST)
        if form.is_valid():
            transcation = form.save(commit=False)
            transcation.user= request.user
            transcation.save()
            return redirect('dashboard')
        else:
            return render(request,'finance/transcation_form.html',{'form':form})
class TransactionList(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        transactions = TransactionModel.objects.all()
        return render(request,'finance/transcation_list.html',{'transactions':transactions})
    
class GoalView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form = GoalForm()
        return render(request,'finance/set_goal.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            tran_goal = form.save(commit=False)
            tran_goal.user = request.user
            tran_goal.save()
            return redirect('dashboard')
        return render(request,'finance/set_goal.html',{'form':form})
            
        
