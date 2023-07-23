from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    if 'q' in request.GET:
        query = request.GET['q']
        products = Product.objects.filter(name__icontains=query)
        
        # Check if the search query contains "Model"
        if 'Model' in query:
            # Retrieve the "MobileCharger" product from the database
            recommended_product = Product.objects.get(name__iexact='MobileCharger')
        else:
            # Provide a default recommended product if the search query doesn't match any condition
            recommended_product = None

        return render(request, 'home.html', {'products': products, 'query': query, 'recommended_product': recommended_product})
    else:
        products = Product.objects.all()
        return render(request, 'home.html', {'products': products})
        
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    mobile_connector = get_object_or_404(Product, pk=11)
    context = {
        'product': product,
        'mobile_connector': mobile_connector,
    }
    return render(request, 'products/product_details.html', context)

@require_POST
def rate_product(request):
    product_id = request.POST.get("product_id")
    rating = request.POST.get("rating")

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"success": False})
        
    product.rating = rating
    product.save()

    return JsonResponse({"success": True})