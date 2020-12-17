from django.urls import path
from . import views
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('singup', views.Singup.as_view(), name="singup"),
    path('login', views.Login.as_view(), name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',views.Cart.as_view(),name='cart'),
    path('check-out' , views.CheckOut.as_view(),name='checkout'),
    path('order', auth_middleware(views.OrderView.as_view()), name='order')
]
