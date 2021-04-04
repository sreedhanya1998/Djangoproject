from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.category_name

class Expense(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.IntegerField()
    notes=models.CharField(max_length=120,null=True)
    user=models.CharField(max_length=120)
    date=models.DateField()

    def __str__(self):
        return self.user