from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','image',  'category', )
admin.site.register(CATEGORY)
admin.site.register(Cart)
admin.site.register(CartProduct)


