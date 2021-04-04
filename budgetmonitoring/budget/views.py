from django.shortcuts import render,redirect
from budget.forms import BudgetRegistrationForm,ExpenseCreationForm,ExpenseSearchForm,ReviewForm
from django.contrib.auth import authenticate,login,logout
from .models import Expense
from django.db.models import Sum,aggregates
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def signin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request,"budget/homepage.html")
        else:
            return render(request,"budget/login.html",{"message":"invalid credentials"})
    return render(request,"budget/login.html")
def registration(request):
    form=BudgetRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BudgetRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"]=form
            return render(request, "budget/registration.html", context)
    return render(request,"budget/registration.html",context)
def signout(request):
    logout(request)
    return redirect("signin")
@login_required
def expense_create(request):
    form=ExpenseCreationForm(initial={'user':request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ExpenseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addexpense")
        else:
            context["form"] = form
            return render(request, "budget/expense_create.html", context)
    return render(request,"budget/expense_create.html",context)
@login_required
def view_expense(request):
    form=ExpenseSearchForm()
    # date=form.cleaned_data.get(date=date)
    context={}
    context["form"]=form
    expenses=Expense.objects.filter(user=request.user)
    context["expenses"]=expenses
    if request.method=="POST":
        form=ExpenseSearchForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data.get("date")
            expenses=Expense.objects.filter(date=date,user=request.user)
            context["expenses"]=expenses
            return render(request,"budget/view_expense.html",context)

    return render(request,"budget/view_expense.html",context)
@login_required
def edit_expense(request,id):
    expense=Expense.objects.get(id=id)
    form=ExpenseCreationForm(instance=expense)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ExpenseCreationForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect("viewexpense")
        else:
            form=ExpenseCreationForm()
            context["form"]=form
            return redirect("viewexpense")
    return render(request,"budget/edit_expense.html",context)
@login_required
def delete_expense(request,id):
    Expense.objects.get(id=id).delete()
    return redirect("viewexpense")
def review_expense(request):
    form=ReviewForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            frm_date=form.cleaned_data.get("from_date")
            to_date = form.cleaned_data.get("to_date")
            total=Expense.objects.filter(date__gte=frm_date,date__lte=to_date,user=request.user).aggregate(Sum("amount"))
            context["total"]=total["amount__sum"]
            return render(request, "budget/review.html", context)
    return render(request,"budget/review.html",context)
