from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    cat_name = models.CharField(max_length=25)

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subcat_name

class Product(models.Model):
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_name = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="productImg")

    def __str__(self):
        return  self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    msg = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField()

class Order(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email = models.EmailField()
    products = models.CharField(max_length=500)
    order_id = models.CharField(max_length=200)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    pay_s = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.fname
    


    




