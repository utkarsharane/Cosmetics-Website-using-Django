from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

# -------------------------------------------------Categories section-------------------------------------------------

class CustomManager(models.Manager):
    def makeup(self):
        return self.filter(category__exact="Makeup")
    
    def haircare(self):
        return self.filter(category__exact="Haircare")
    
    def skincare(self):
        return self.filter(category__exact="Skincare")
    
    def appliances(self):
        return self.filter(category__exact="Appliances")

# -----------------------------------------------Product section------------------------------------------------------

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=55)
    type = (("Makeup","Makeup"),("Haircare","Haircare"),("Skincare","Skincare"),("Appliances","Appliances"))
    category = models.CharField(max_length=100,choices=type,default="")
    desc = models.TextField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="pics")
    objects = models.Manager()
    prod = CustomManager()

# ---------------------------------------------------Cart section-------------------------------------------------------

class Bag(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

# -----------------------------------------------Wishlist section------------------------------------------------------

class Wishlist(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

# -----------------------------------------------Blog section----------------------------------------------------------
    
class RegisterBlog(models.Model):
    photo = models.ImageField(upload_to="images", default="none")
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def coverphoto(self):
        return mark_safe(f'<img src="{self.photo.url}" width="100px"/')
    
# -----------------------------------------------Order section----------------------------------------------------------


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)



