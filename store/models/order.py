from django.db import models
from .product import  Product
from .customer import  Customer
import datetime
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=11,default='',blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"Product: {self.product.first_name} ____ customer: {self.customer.first_name} {self.customer.last_name}"
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
