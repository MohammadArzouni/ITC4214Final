from django.shortcuts import render
from products.models import Product

# Create your views here.

def home_page(request):
    search_query = request.GET.get('q')
    max_price = request.GET.get('max_price')

    # Filter the products based on the search query and max_price
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products
    }
    return render(request, 'home.html', context)