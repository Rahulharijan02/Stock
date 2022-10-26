from django.contrib import admin
from .models import query, stock
# Register your models here.

@admin.register(query)
class StockAdmin(admin.ModelAdmin):
 list_display = ['id','username', 'stockname', 'query']


@admin.register(stock)
class StockAdmin(admin.ModelAdmin):
 list_display = ['id','stockname', 'image', 'description']
 




 
