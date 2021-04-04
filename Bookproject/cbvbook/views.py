from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .models import Book
from .forms import BookCreateForm
from django.urls import reverse_lazy
# Create your views here.
class book_list(ListView):
    model=Book
    context_object_name = 'books'
    template_name = "cbvbook/book_list.html"
class book_detail(DetailView):
    model=Book
    template_name = "cbvbook/book_detail.html"
# create,update,delete
class book_create(CreateView):
    model=Book
    form_class = BookCreateForm
    template_name = "cbvbook/book_create.html"
    success_url = reverse_lazy("list")
class book_update(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = "cbvbook/bookupdate.html"
    success_url = reverse_lazy("list")
class book_delete(DeleteView):
    model=Book
    template_name = "cbvbook/bookdelete"
    success_url = reverse_lazy("list")
class list_book(TemplateView):
    model=Book
    context={}
    template_name = "cbvbook/book_list.html"
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)
class detail_book(TemplateView):
    model=Book
    context={}
    template_name = "cbvbook/book_detail.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        books=self.model.objects.get(id=id)
        self.context["books"]=books
        return render(request,self.template_name,self.context)
