from django.shortcuts import render,redirect
from products.models import Products,Botella1l
from products.forms import Formulario_birras


def create_product(request):
    
    if request.method == "POST":
        form = Formulario_birras(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data["name"],
                style = form.cleaned_data["style"],
                alcohol_volume =form.cleaned_data["alcohol_volume"],
                IBU = form.cleaned_data["IBU"],
                description = form.cleaned_data["description"],
                malt = form.cleaned_data["malt"],
                hop = form.cleaned_data["hop"],
                price = form.cleaned_data["price"],
                creation_date = form.cleaned_data["creation_date"],
                is_active = form.cleaned_data["is_active"],
            )
            return redirect(products_list) # lo que hace redireccionar a list_producs

    elif request.method == "GET":
        form = Formulario_birras()
        context = {"form":form}
        return render(request,"products/new_product.html", context=context)





def create_1l(request):
    new_botella = Botella1l.objects.create(
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
        "botella1l" : new_botella
    }
    return render(request,"products/botella1l.html", context=context)





def products_list(request):
    products = Products.objects.all()
    context = {
        "products" : products
    }
    return render(request,"products/products_list.html", context=context)
