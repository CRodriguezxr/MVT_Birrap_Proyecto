from django.shortcuts import render
from products.models import Products,Botella_1l,Botella_lata_473cc

def create_product(request):
    new_product = Products.objects.create(
        name = "Amber Lager",
        style = "Lager",
        alcohol_volume = 6,
        IBU = 4,
        description = "Es una cerveza con una combinación de lúpulos patagónicos y un blend de finas maltas que generan su color rojizo,un delicado aroma y un amargor apacible que permite dar a luz a un tostado delicioso.",
        malt = "Caramelo",
        hop = "Hercules",
        price = 480,
        creation_date = "", 
        is_active = True,
    )
    context = {
        "new_product" : new_product
    }
    return render(request,"products/new_product.html", context=context)

def products_list(request):
    products = Products.objects.all()
    context = {
        "products" : products
    }
    return render(request,"products/products_list.html", context=context)



def crear_botella1l(request):
    new_botella_1l = Botella_1l.objects.create(
        name = "Amber Lager",
        style = "lager",
        alcohol_volume = 6,
        IBU = 4,
        description = "Es una cerveza con una combinación de lúpulos patagónicos y un blend de finas maltas que generan su color rojizo,un delicado aroma y un amargor apacible que permite dar a luz a un tostado delicioso.",
        malt = "Caramelo",
        hop = "Hercules",
        price = 480,
        creation_date = "", 
        is_active = True,
    )
    context = {
        "new_botella_1l" : new_botella_1l
    }
    return render(request,"products/new_botella_1l.html", context=context)

def lista_botella_1l(request):
    botellas_1l = Botella_1l.objects.all()
    context = {
        "botellas_1l" : botellas_1l
    }
    return render(request,"products/botellas_1l.html", context=context)



def crear_botella_lata_473cc(request):
    new_botella_lata_473cc = Botella_lata_473cc.objects.create(
        name = "Amber Lager",
        style = "lata",
        alcohol_volume = 6,
        IBU = 4,
        description = "Es una cerveza con una combinación de lúpulos patagónicos y un blend de finas maltas que generan su color rojizo,un delicado aroma y un amargor apacible que permite dar a luz a un tostado delicioso.",
        malt = "Caramelo",
        hop = "Hercules",
        price = 480,
        creation_date = "", 
        is_active = True,
    )
    context = {
        "new_botella_lata_473cc" : new_botella_lata_473cc
    }
    return render(request,"products/new_botella_lata_473cc.html", context=context)

def lista_botella_lata_473cc(request):
    botellas_lata_473cc = Botella_lata_473cc.objects.all()
    context = {
        "botellas_lata_473cc" : botellas_lata_473cc
    }
    return render(request,"products/botellas_lata_473cc.html", context=context)
