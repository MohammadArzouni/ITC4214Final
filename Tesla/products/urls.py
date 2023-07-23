from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('rate_product/', views.rate_product, name='rate_product'),
]
