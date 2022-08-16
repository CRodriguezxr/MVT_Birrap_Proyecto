from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import Products,Botella_1l,Botella_lata_473cc
from products.forms import Formulario_botellas1lt, Formulario_latas473cc, Formulario_botellas500cc


# def create_product(request):
#     new_product = Products.objects.create(
#         name = "Amber Lager",
#         style = "Lager",
#         alcohol_volume = 6,
#         IBU = 4,
#         description = "Es una cerveza con una combinación de lúpulos patagónicos y un blend de finas maltas que generan su color rojizo,un delicado aroma y un amargor apacible que permite dar a luz a un tostado delicioso.",
#         malt = "Caramelo",
#         hop = "Hercules",
#         price = 480,
#         creation_date = "", 
#         is_active = True,
#     )
#     context = {
#         "new_product" : new_product
#     }
#     return render(request,"products/new_product.html", context=context)



def products_list(request):
    products = Products.objects.all()
    context = {
        "products" : products
    }
    return render(request,"products/products_list.html", context=context)


def crear_botella_500cc(request):

    if request.method == 'POST':
     form = Formulario_botellas500cc(request.POST)

     if form.is_valid():
        Products.objects.create(
             name = form.cleaned_data['name'],
             style = form.cleaned_data['style'],
             alcohol_volume = form.cleaned_data['alcohol_volume'],
             IBU = form.cleaned_data['IBU'],
             description = form.cleaned_data['description'],
             malt = form.cleaned_data['malt'],
             hop = form.cleaned_data['hop'],
             price = form.cleaned_data['price'],
             creation_date = form.cleaned_data['creation_date'], 
             is_active = form.cleaned_data['is_active']
        )
        return redirect(products_list) 
    
    elif request.method == 'GET':
        form = Formulario_botellas500cc()
        context = {'form':form}
        return render(request,"products/new_botella_500cc.html", context=context)


def buscar_birra500(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    context = {'products':products}
    return render(request, 'products/buscar_birra500.html', context=context)


def delete_birra_500cc(request,pk):
    if request.method == "GET":
        product = Products.objects.get(id = pk)
        context = {"product":product}
        return render (request,"products/delete_birra_500cc.html",context = context)
    elif request.method == "POST":
        product = Products.objects.get(id = pk)
        product.delete()
        return redirect(products_list)










def crear_botella1l(request):
   if request.method == 'POST':
     form = Formulario_botellas1lt(request.POST)

     if form.is_valid():
        Botella_1l.objects.create(
             name = form.cleaned_data['name'],
             style = form.cleaned_data['style'],
             alcohol_volume = form.cleaned_data['alcohol_volume'],
             IBU = form.cleaned_data['IBU'],
             description = form.cleaned_data['description'],
             malt = form.cleaned_data['malt'],
             hop = form.cleaned_data['hop'],
             price = form.cleaned_data['price'],
             creation_date = form.cleaned_data['creation_date'], 
             is_active = form.cleaned_data['is_active']
        )
        return redirect(lista_botella_1l) 
    
   elif request.method == 'GET':
    form = Formulario_botellas1lt()
    context = {'form':form}
    return render(request, 'products/new_botella_1l.html', context = context )
   

def lista_botella_1l(request):
    botellas_1l = Botella_1l.objects.all()
    context = {
        "botellas_1l" : botellas_1l
    }
    return render(request,"products/botellas_1l.html", context=context)


def buscar_birra1l(request):
    search= request.GET['search']
    botellas_1l= Botella_1l.objects.filter(name__icontains= search)
    context = {'botellas_1l':botellas_1l}
    return render(request, 'products/buscar_birra1l.html', context=context)


def delete_birra_1l(request,pk):
    if request.method == "GET":
        botellas_1l = Botella_1l.objects.get(id = pk)
        context = {"botellas_1l":botellas_1l}
        return render (request,"products/delete_birra1l.html",context = context)
    elif request.method == "POST":
        product = Botella_1l.objects.get(id = pk)
        product.delete()
        return redirect(lista_botella_1l)










def crear_lata_473cc(request):
    if request.method == 'POST':
     form = Formulario_latas473cc(request.POST)

     if form.is_valid():
        Botella_lata_473cc.objects.create(
             name = form.cleaned_data['name'],
             style = form.cleaned_data['style'],
             alcohol_volume = form.cleaned_data['alcohol_volume'],
             IBU = form.cleaned_data['IBU'],
             description = form.cleaned_data['description'],
             malt = form.cleaned_data['malt'],
             hop = form.cleaned_data['hop'],
             price = form.cleaned_data['price'],
             creation_date = form.cleaned_data['creation_date'], 
             is_active = form.cleaned_data['is_active']
        )
        return redirect(lista_botella_lata_473cc) 
    
    elif request.method == 'GET':
        form = Formulario_latas473cc()
        context = {'form':form}
        return render(request,"products/new_lata_473cc.html", context=context)


def lista_botella_lata_473cc(request):
    botellas_lata_473cc = Botella_lata_473cc.objects.all()
    context = {
        "botellas_lata_473cc" : botellas_lata_473cc
    }
    return render(request,"products/botellas_lata_473cc.html", context=context)


def buscar_lata_473cc(request):
    search= request.GET['search']
    latas_473cc= Botella_lata_473cc.objects.filter(name__icontains= search)
    context = {'latas_473cc':latas_473cc}
    return render(request, 'products/buscar_lata_473cc.html', context=context)



def delete_lata_473cc(request,pk):
    if request.method == "GET":
        latas_473cc = Botella_lata_473cc.objects.get(id = pk)
        context = {"latas_473cc":latas_473cc}
        return render (request,"products/delete_latas_473cc.html",context = context)
    elif request.method == "POST":
        product = Botella_lata_473cc.objects.get(id = pk)
        product.delete()
        return redirect(lista_botella_lata_473cc)