from django.shortcuts import render
from products.models import Products

def create_product(request):
    new_product = Products.objects.create(
        name = "Golden Argenta",
        style = "Ale",
        alcohol_volume = 5,
        IBU = 3,
        description = "Esta cerveza Rubia de estilo ingles, muy balanceada, ""\n""de color dorado y excelente cuerpo gracias a la combinación ""\n""de maltas pálidas y maltas acarameladas.",
        malt = "Pálida",
        hop = "Cascade",
        price = 480,
        creation_date = "", 
        is_active = True,
    )
    context = {
        "new_product" : new_product
    }
    return render(request,"new_product.html", context=context)
