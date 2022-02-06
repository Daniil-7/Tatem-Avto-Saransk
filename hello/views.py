from django.shortcuts import render
from .models import *

def index(request):
  context = {
    'categorys': Category.objects.all()
  }
  return render(request, "index.html", context)


def category_page(request, category_id_src):
  context = {
    'products': Product.objects.filter(category=category_id_src),
    'categorys': Category.objects.all()
  }
  return render(request, 'category_page.html', context)


def product_page(request, product_id_src):
  context = {
    'products': Product.objects.filter(product_category_id=product_id_src),
    'categorys': Category.objects.all()
  }
  return render(request, 'product_page.html', context)