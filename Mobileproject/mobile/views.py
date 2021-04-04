from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import CreateForm,MobileCateForm,Customerform,Mobilestatusform,Status,Mobilesearchform,Paymentform
from .models import MobileOrder
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def mobile_registration(request):
    form=CreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"mobile/signin.html")
    return render(request,"mobile/register.html",context)
def signin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request,"mobile/base.html")
        else:
            return render(request,"mobile/signin.html",{"message":"invalide credentials"})
    return render(request,"mobile/signin.html")
def signout(request):
    logout(request)
    return redirect("signin")
def create_mobile(request):
    form=MobileCateForm()
    mobile=MobileOrder.objects.all()
    context={}
    context["form"]=form
    context["mobile"]=mobile
    if request.method=="POST":
        form=MobileCateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "mobile/mobilelist.html", context)
    return render(request,"mobile/mobilecreate.html",context)
def mobile_list(request):
    form=Mobilestatusform()
    mobile = MobileOrder.objects.all()
    context={}
    context["form"]=form
    context["mobile"] = mobile
    if request.method=="POST":
        form=Mobilestatusform(request.POST)
        if form.is_valid():
            status=form.cleaned_data.get("status")
            mobile=MobileOrder.objects.filter(status__status=status)
            context["mobile"]=mobile
            return render(request, "mobile/mobilesearch.html", context)
            # min_price = form.cleaned_data.get("price1")
            # max_price = form.cleaned_data.get("price2")
            # mobile = MobileOrder.objects.filter(price__gte=min_price, price__lte=max_price)
    return render(request, "mobile/mobilelist.html", context)
def mobile_edit(request,id):
    mobile = MobileOrder.objects.get(id=id)
    form=MobileCateForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCateForm(request.POST,instance=mobile)
        if(form.is_valid()):
            form.save()
            return render(request, "mobile/mobilelist.html", context)
    return render(request,"mobile/mobileedit.html",context)

def mobile_view(request,id):
    mobile=MobileOrder.objects.get(id=id)
    context = {}
    context["mobile"] = mobile
    return render(request, "mobile/mobileview.html", context)
def status_Check(request):
    form=Customerform()
    context={}
    context["form"]=form
    if request.method == "POST":
            form=Customerform(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "mobile/payment.html")
    return render(request, "mobile/customer.html",context)
def sucess(request):
    return render(request, "mobile/sucess.html")

def payment(request):
    form=Paymentform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Paymentform(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'mobile/sucess.html')
        else:
            return render(request, "mobile/failed.html")
    return render(request,'mobile/payment.html',context)
def loginpage(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        user=authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request,"mobile/mainpage.html")
        else:
            return render(request,"mobile/login.html",{"message":"invalide credentials"})
    return render(request,"mobile/login.html")
def mainlist(request):
    mobile = MobileOrder.objects.all()
    context={}
    context["mobile"] = mobile
    return render(request, "mobile/mainlist.html", context)


