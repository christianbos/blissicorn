from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'slug', 'modelo', 'descripcion', 'precio', 'stock')
	list_filter = ('modelo', 'precio')
	search_fields = ('nombre', 'descripcion')
	prepopulated_fields = {'slug': ('nombre',)}
	ordering = ['precio']

admin.site.register(Product, ProductAdmin)