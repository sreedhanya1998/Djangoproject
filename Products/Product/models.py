from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=120)
    product_no=models.IntegerField()
    price=models.IntegerField(default=50)
    expiry_date=models.CharField(max_length=120)

    def __str__(self):
        return self.product_name