from django.shortcuts import render
from home.models import Articles

def create_article(request):
    new_article = Articles.objects.create(
        title = "Kaia HomeBrewers - Quienes somos",
        description_1 = "Desde los comienzos la misión fue elaborar una cerveza de alta calidad, de gran variedad y combinaciones. /n Y de esta manera, poder satisfacer a un consumidor más exigente y conocedor del mundo de las “Buenas Cervezas”.",
        description_2 = "La cerveza Kaia es un producto Premium que se destaca por una gran gama de sabores y estilos. /n Su calidad ha logrado que los comercios la quieran tener por ser un producto tradicional y exótico, debido a su origen y variedades premium",
        team = "Kaia HomeBrewers: Somos apasionados por la cerveza artesanal que se esmeran día a día para hacer las cervezas más ricas, mejorar la calidad, ser innovadores, creativos y brindarle a nuestros clientes más de lo que esperan. ",
        author = "Claudio Rodriguez - Ignacio Ramos - Axel Bermudez",

    )
    context = {
        "new_article" : new_article
    }
    return render(request,"new_article.html", context=context)

