from django.db import models

# Create your models here.


from django.db import models
from django.db.models import Model
# Create your models here.
class mobile_detail(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    # price=models.CharField(max_length=120)
    # memory=models.CharField(max_length=120)
    #
    def __str__(self):
        return self.mobile_name
class Status(models.Model):
    status=models.CharField(max_length=120)
    def __str__(self):
        return self.status
class MobileOrder(models.Model):
    mobile_image=models.ImageField(upload_to="images")
    mobile_name=models.ForeignKey(mobile_detail,on_delete=models.CASCADE)
    price=models.CharField(max_length=120)
    memory=models.CharField(max_length=120)
    size=models.CharField(max_length=120)
    Battery=models.CharField(max_length=120)
    Warranty=models.CharField(max_length=120)
    status=models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.mobile_name
class Customer(models.Model):
    customer_name=models.CharField(max_length=120)
    phone_no=models.IntegerField()
    Address=models.CharField(max_length=120)

    def __str__(self):
        return self.customer_name

class Paymentinfo(models.Model):
    holder_name=models.CharField(max_length=120)
    account_no=models.DecimalField(max_digits=18,decimal_places=0)
    IFSC_code=models.CharField(max_length=50)
    cvv=models.IntegerField()

    def __str__(self):
        return self.holder_name
