from django.shortcuts import render, redirect
from .models import Product
from campaings.models import Campaing
from django.http import HttpResponse
from .forms import CreateNewProduct

# Create your views here.

def products(request):
    return render(request, "products/list_products.html", {
        'productos': Product.objects.all()
    })

def products_by_campaing(request,campaing_id):
    return render(request, "products/list_products.html", {
        'productos': Product.objects.filter(campaing_id = campaing_id),
        'campaing_id': campaing_id
    })

def modificar_products(request):
    return HttpResponse("Something")

def new_product(request, campaing_id):
    if request.method == 'GET':
        return render(request, "products/new_product.html",{
            'form': CreateNewProduct,
            'campaing_id': campaing_id
        })
    else:
        Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price'],
            campaing_id = campaing_id
            )
        return redirect(f'/products/{campaing_id}')
    
def delete_product(request,campaing_id,product_id):
    Product.objects.filter(id = product_id).delete()
    return redirect(f'/products/{campaing_id}')

def edit_product(request,campaing_id,product_id):
    if request.method == 'GET':
        product_queryset = Product.objects.filter(id = product_id)
        if(product_queryset.exists()):
            product = product_queryset.first()
            initial_data = {
                'name' : product.name,
                'description' : product.description,
                'price': product.price
            }
        return render(request, "products/edit_product.html",{
            'form': CreateNewProduct(initial=initial_data),
        })
    else:
        if request.method == 'POST' and request.POST.get('_method') == 'PUT':
            Product.objects.filter(id = product_id).update(
                name = request.POST['name'],
                description = request.POST['description'],
                price = request.POST['price']
            )
        return redirect(f'/products/{campaing_id}')
