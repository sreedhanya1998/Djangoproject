# from django.shortcuts import render,redirect
# from Product.forms import ProductCreateForm
# from Product.models import Product
# # Create your views here.
# def product_create(request):
#     form=ProductCreateForm()
#     context={}
#     product=Product.objects.all()
#     context["form"]=form
#     context["product"]=product
#     if request.method=="POST":
#         form=ProductCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("create")
#     return render(request,"Product/createproduct.html",context)



