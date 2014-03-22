from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext
from app.models import *
from app.forms import *

# Create your views here.
def home(request):
	return HttpResponse("Hola mundo desde Win7 con virtualenv parchado XD")

def post(request, id_post):
	post = Post.objects.get(pk=id_post)
	template = 'post.html'
	titulo = post.titulo
	contenido = post.contenido
	comentarios = post.comentario_set.all()
	return render_to_response(template, locals())
	# return HttpResponse("hola mundo 3")

def posts(request):
	posts = Post.objects.all()
	template = 'post/index.html'
	return render_to_response(template, locals())

def add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			form = PostForm()
	template = "post/form.html"
	return render_to_response(template,
		context_instance = RequestContext(request, locals()))