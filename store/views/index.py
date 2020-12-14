from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request):
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
            'cart': request.session.get('cart')
        }
        return render(request, 'store/index.html', template_var)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quentity = cart.get(product)
            if quentity:
                if remove:
                    if quentity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quentity - 1
                else:
                    cart[product] = quentity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        print(cart)
        request.session['cart'] = cart
        return redirect('homepage')
