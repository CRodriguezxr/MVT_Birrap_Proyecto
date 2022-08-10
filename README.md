# MVT_Birrap_Proyecto

Colaboradores Claudio Rodriguez, Ignacio Ramos, Axel Bermudez.

El proyecto consta de un e-commerce de cervezas artesanales el cual muestra 3 clases de productos : Botellas de 1l, botellas de 500cc y latas de 473cc.

Para crear cada una ir a las urls que contiene cada una un formulario

<p>http://127.0.0.1:8000/products/crear_botella1l/ para las de 1l</p>
<p>http://127.0.0.1:8000/products/crear_botella_500/ para 500cc</p>
<p>http://127.0.0.1:8000/products/crear_botella_lata_473cc/ para las latas</p>

se crean mediante las funciones que estan en el archivo products/views.py y los formularios ubicados en products/forms.py

y pueden ser vistas en los siguientes urls>

<p>http://127.0.0.1:8000/products/lista_botella_lata_473cc/</p>
<p>http://127.0.0.1:8000/products/lista_botella_1l/</p>
<p>http://127.0.0.1:8000/products/products_list/</p>

donde cada url carga su template .html correspondiente

se realizo un formulario ubicado en el navbar para la busqueda de productos
