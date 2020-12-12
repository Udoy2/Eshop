from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.views import View


class Singup(View):
    def get(self, request):
        return render(request, "singup.html")

    def post(self, request):
        return self.registerCoustomer(request)

    def registerCoustomer(self, request):
        # post data action --------------------------------
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
        # object of coustomer creation
        coustomer = Customer(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)

        # validation
        error_message = self.validateCustomer(coustomer)

        if error_message == None:
            coustomer.password = make_password(coustomer.password)
            coustomer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, "singup.html", data)

    def validateCustomer(self, customer):
        # validation
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif customer.email:
            if len(customer.email) < 5:
                error_message = 'Email must be 5 char long'
            elif customer.isExists():
                error_message = 'Email Address Already Registered!!'

        return error_message;
