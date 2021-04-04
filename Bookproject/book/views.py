from django.shortcuts import render,redirect
from book.forms import BookCreateForm,BookUpdateForm
from book.models import Book

# Create your views here.
def home(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    return render(request,"book/index.html",context)

def book_create(request):
    form=BookCreateForm()
    context={}
    books=Book.objects.all()
    context["books"]=books
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("create")
        else:
            context["form"]=form
            return render(request,"book/bookcreate.html",context)
    return render(request,"book/bookcreate.html",context)
def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,'book/bookview.html',context)
def book_delete(request,id):
    Book.objects.get(id=id).delete()
    return redirect("create")
def book_edit(request,id):
    book=Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request,"book/bookedit.html",context)