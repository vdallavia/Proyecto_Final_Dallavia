from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from TecnoBlog_App.forms import ArticuloFormulario
from TecnoBlog_App.models import Articulo, AcercaDeMi

# Create your views here.

# Vista de Inicio
def inicio(request):
    contexto = { }
    http_response=render(
        request=request,
        template_name="TecnoBlog_App/base.html",
        context=contexto,
    )
    return http_response

# Vista de Acerca de Mi
def acerca_de_mi(request):
    sobre_mi = AcercaDeMi.objects.first()  #para obtener el objeto 
    contexto = {'sobre_mi': sobre_mi}
    http_response=render(
        request=request,
        template_name="TecnoBlog_App/acerca_de_mi.html",
        context=contexto,
    )
    return http_response

# Vista de articulos
def listar_articulos(request):
    contexto = { 
        "articulos": Articulo.objects.all()
    }
    http_response=render(
        request=request,
        template_name="TecnoBlog_App/lista_articulos.html",
        context=contexto,
    )
    return http_response

def detallar_articulo(request, id):
    try:
        articulo = Articulo.objects.get(id=id)
        contexto = {
            "articulo": articulo
        }
        return render(request, "TecnoBlog_App/detalle_articulo.html", contexto)
    except Articulo.DoesNotExist:
        return redirect('listar_articulos')

# Vista de Crear articulos
@login_required
def crear_articulo(request):
    #print(f"HOLA, estoy en crear articulo y el request es: {request}")
    if request.method == "POST":
        #print("11111111111111111111111111111111111111111")
        #print(request.POST)
        #print(request.FILES)
        #print(request.FILES['imagen'])
        formulario = ArticuloFormulario(request.POST)
        #print(formulario.is_bound)
        #print(formulario.errors)
        if formulario.is_valid():
            #print("222222222222222222222222222222222222222222")
            data = formulario.cleaned_data  # es un diccionario
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            autor = data["autor"]
            fecha = data["fecha"]
            imagen = data["imagen"]
            #print(imagen)
            imagen = request.FILES['imagen']
            descripcion = data["descripcion"]
            creador = request.user
            articulo = Articulo(creador=creador, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen, descripcion=descripcion)
            articulo.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de articulos
            url_exitosa = reverse('listar_articulos')
            #print("33333333333333333333333333333333")
            return redirect(url_exitosa)
        else:
            #print("44444444444444444444444444444")
            return redirect('/articulos')
    else:
        #print("555555555555555555555")
        formulario = ArticuloFormulario()
        http_response = render(
              request=request,
              template_name='TecnoBlog_App/articulo_formulario.html',
              context={'formulario': formulario}
            )
        #print("666666666666666666666666")
        return http_response


# Vista de eliminar articulo
@login_required
def eliminar_articulo(request, id):
    articulo_eliminar = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo_eliminar.delete()
        url_exitosa = reverse('listar_articulos')
        return redirect(url_exitosa)


 # Vista de editar articulo
@login_required
def editar_articulo(request, id):
    articulo_editar = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo_editar.titulo = data["titulo"]
            articulo_editar.subtitulo = data["subtitulo"]
            articulo_editar.cuerpo = data["cuerpo"]
            articulo_editar.autor = data["autor"]
            articulo_editar.fecha = data["fecha"]
            articulo_editar.imagen = data["imagen"]
            articulo_editar.descripcion = data["descripcion"]
            articulo_editar.save()

            url_exitosa = reverse('detalle-articulos')
            return redirect(url_exitosa)
    
    else: # GET
        inicial = {
            'titulo': articulo_editar.titulo,
            'subtitulo': articulo_editar.subtitulo,
            'cuerpo': articulo_editar.cuerpo,
            'autor': articulo_editar.autor,
            'fecha': articulo_editar.fecha,
            'imagen': articulo_editar.imagen,
            'descripcion': articulo_editar.descripcion,
        }
        formulario = ArticuloFormulario(initial=inicial)

    return render(
        request=request,
        template_name='TecnoBlog_App/articulo_formulario.html',
        context={'formulario': formulario},
    )
