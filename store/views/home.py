from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


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
        'products': products,
        "categorys": categorys,
    }
    return render(request, 'store/index.html', template_var)
