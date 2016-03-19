from django.shortcuts import render
from django.views.generic import View
from .models import Product
from .forms import ProductForm

class HomeView(View):
	def get(self, request):
		template_name = "productos/todos.html"
		productos = Product.objects.all()
		form = ProductForm()
		context = {
		'productos' : productos,
		'form' : form
		}
		return render(request, template_name, context)

	def product(self,request):
		form = ProductForm(request.POST)
		form.save()
		return redirect('productos:todos')

class ProductDetailView(View):
    def get(self, request, id):
        template_name = "productos/detalle.html"
        post = Product.objects.get(pk = id)
        context = {"posts":post}
        return render(request, template_name, context)