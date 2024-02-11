from django.contrib import admin
from .models import Product,Bag,Wishlist,RegisterBlog,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_id","product_name","price","category","image"]

class BagAdmin(admin.ModelAdmin):
    list_display = ["product_id", "qty","userid"]

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["product_id","userid"]

class Blogadmin(admin.ModelAdmin):
    list_display =["coverphoto","title", "name","description"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id","userid","product_id","qty"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Bag,BagAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(RegisterBlog,Blogadmin)
admin.site.register(Order, OrderAdmin)
