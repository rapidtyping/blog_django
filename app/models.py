from django.db import models

# Create your models here.
class Post(models.Model):
	titulo 	  = models.CharField(max_length = 140)
	contenido = models.TextField()
	creado	  = models.DateTimeField(blank=False)	
	actualizado = models.DateTimeField(blank=False)
	
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	comentador = models.CharField(max_length = 50)
	body       = models.TextField()
	post_id    = models.ForeignKey(Post)

	def __unicode__(self):
		return self.comentador
