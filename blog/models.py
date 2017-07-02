from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    image_for_preview = models.ImageField(upload_to='img')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    categoria = models.CharField(max_length=256, choices=[('Tramites', 'Tramites'), ('Info', 'Info'), ('Exp', 'Exp')], null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Infolink(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    image_for_preview = models.ImageField(upload_to='img',blank=True)
    published_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

# FALTA PREVIEW IMAGE EN EL BIGCONTAINER Y EN EL TEMPLATE FALTA AGREGARLO TAMBIEN. ADEMAS FALTA METODO EN Bigc
# title equivale a un objeto post
# esto es el container, seleccionas en un dropdown menu el post que quieres ver de container
# como title es objeto ahora, title.title sera el titulo del objeto title, que sera un post. El titulo de un post
# el resto, de igual forma, title.text sera el atributo text del objecto post, que es el texto de un post
class Bigc(models.Model):
    title = models.ForeignKey('blog.Post')
    categoria = None
    text = None
    published_date = None
    image_preview = models.ImageField(default="img/default.png", upload_to='img', blank=False, help_text = "Imagenes deben ser de una resolucion: 600px ancho, 400px de alto. Esto para evitar inconvenientes")
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title.title
    def get_text(self):
        return self.title.text
    def get_categoria(self):
        return self.title.categoria