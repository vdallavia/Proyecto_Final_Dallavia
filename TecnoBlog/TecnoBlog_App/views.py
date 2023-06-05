from django.shortcuts import render, redirect
from django.urls import reverse

from TecnoBlog_App.forms import ArticuloFormulario
from TecnoBlog_App.models import Articulo

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
    contexto = {
    }
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
def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            autor = data["autor"]
            fecha = data["fecha"]
            imagen = data["imagen"]
            imagen = request.FILES['imagen']
            descripcion = data["descripcion"]
            creador = request.user
            articulo = Articulo(creador=creador, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen, descripcion=descripcion)
            articulo.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de articulos
            url_exitosa = reverse('listar_articulos')
            return redirect(url_exitosa)
        else:
            return redirect('/articulos')
    else:
        formulario = ArticuloFormulario()
        http_response = render(
              request=request,
              template_name='TecnoBlog_App/articulo_formulario.html',
              context={'formulario': formulario}
            )
        return http_response


# Vista de eliminar articulo
def eliminar_articulo(request, id):
    articulo_eliminar = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo_eliminar.delete()
        url_exitosa = reverse('listar_articulos')
        return redirect(url_exitosa)

 # Vista de editar articulo
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
            articulo_editar.imagen = request.FILES["imagen"]
            articulo_editar.descripcion = data["descripcion"]
            articulo_editar.save()

            url_exitosa = reverse('detallar_articulo', kwargs={'id': articulo_editar.id})
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
        context={'formulario': formulario}
    )