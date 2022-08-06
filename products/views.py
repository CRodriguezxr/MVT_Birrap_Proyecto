from django.shortcuts import render
from products.models import Products

def create_product(request):
    new_product = Products.objects.create(
        name = "Amber Lager",
        style = "Lager",
        alcohol_volume = 6,
        IBU = 4,
        description = "Es una cerveza con una combinación de lúpulos patagónicos y un blend de finas maltas que generan su color rojizo,un delicado aroma y un amargor apacible que permite dar a luz a un tostado delicioso./n Ideal para acompañar carnes asadas y pastas con salsas especiadas..",
        malt = "Caramelo",
        hop = "Hercules",
        price = 480,
        creation_date = "", 
        is_active = True,
    )
    context = {
        "new_product" : new_product
    }
    return render(request,"new_product.html", context=context)

def list_products(request):
    products = Products.objects.all()
    context = {
        "products" : products
    }
    return render(request,"products_list.html", context=context)
