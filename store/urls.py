from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('/singup',views.singup,name="singup")
]