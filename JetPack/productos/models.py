from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Product(models.Model):
	nombre = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 50, blank = True, null = True)
	modelo = models.TextField()
	descripcion = models.TextField()
	precio = models.TextField()
	stock = models.TextField()

	def _str_(self):
		return self.nombre