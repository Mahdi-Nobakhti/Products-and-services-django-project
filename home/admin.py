from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Category)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
    search_fields = ['title']


admin.site.register(Product,ProductAdmin)