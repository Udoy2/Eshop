from django.shortcuts import render ,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.order import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_all_products_by_its_id(list(cart.keys()))
        print(address,phone,cart,customer,products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          address=address,
                          phone=phone)
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')


