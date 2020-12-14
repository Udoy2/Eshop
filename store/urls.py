from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('singup', views.Singup.as_view(), name="singup"),
    path('login', views.Login.as_view(), name='login')
]
