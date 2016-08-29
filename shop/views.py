from django.shortcuts import render

from .models import Cathegory, Product


def product_list(request, cathegory_slug=None):
	cathegory = None
	cathegories = Cathegory.objects.all()
	products = Product.objects.filter(available=True)
	
