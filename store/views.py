from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.

def home(request):
    products = None
    categorys = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()
    template_var = {
        'products':products,
        "categorys":categorys,
    }
    return render(request,'store/index.html',template_var)

def singup(request):
    return render(request,"singup.html")
