from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MobileOrder,Customer,Status,Paymentinfo
from django import forms

class CreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password"]

class MobileCateForm(ModelForm):
    class Meta:
        model=MobileOrder
        fields="__all__"

class Customerform(ModelForm):
    class Meta:
        model=Customer
        fields=['customer_name','phone_no','Address']
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control"}),
            "Address": forms.TextInput(attrs={"class": "form-control"})
        }
class Mobilesearchform(forms.Form):
    price1= forms.IntegerField()
    price2= forms.IntegerField()
class Mobilestatusform(forms.Form):
   status=forms.CharField()
class Paymentform(ModelForm):
    class Meta:
        model=Paymentinfo
        fields="__all__"

