from django.forms import ModelForm
from Product.models import Product



class ProductCreateForm(ModelForm):

    class Meta:
        model=Product
        fields="__all__"