
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('create_product', views.createProduct, name='create_product'),

]
