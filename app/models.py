from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    sale = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        
    def __str__(self) :
        return self.product_name

    
class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="categories_product")
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        
    def __str__(self) :
        return self.category_name

class Partners(models.Model):
    partner_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="parteners_category")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="parteners_product")

class Customers(models.Model):
    customer_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)
    
    
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="cart_product")    
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="cart_customer")    
    