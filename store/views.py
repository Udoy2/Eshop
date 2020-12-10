from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.urls import reverse


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


def singup(request):
    if request.method == "GET":
        return render(request, "singup.html")

    postData = request.POST
    first_name = postData.get('first_name')
    last_name = postData.get('last_name')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    values = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    #object of coustomer creation
    coustomer = Customer(first_name=first_name,
                         last_name=last_name,
                         phone=phone,
                         email=email,
                         password=password)

    # validation
    error_message = None;
    if (not first_name):
        error_message = "First Name Required !!"
    elif len(first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not last_name:
        error_message = 'Last Name Required'
    elif len(last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not phone:
        error_message = 'Phone Number required'
    elif len(phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(password) < 6:
        error_message = 'Password must be 6 char long'
    elif email:
        if len(email) < 5:
            error_message = 'Email must be 5 char long'
        elif coustomer.isExists():
            error_message = 'Email Address Already Registered!!'

    if error_message == None:
        coustomer.register()
        return redirect('homepage')
    else:
        data = {
            'error': error_message,
            'values': values
        }
        return render(request, "singup.html", data)
