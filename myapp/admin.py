from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Register)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Order)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','cat_name','subcat_name','price']