from django.shortcuts import render ,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids = [int(id) for id in request.session.get('cart').keys()]
        products = Product.get_all_products_by_its_id(ids)
        data = {
            'products' : products,
        }
        return render(request, 'cart.html',data)

