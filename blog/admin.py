from django.contrib import admin
from .models import Post, Comment
from .models import Infolink
from .models import Bigc
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Infolink)
admin.site.register(Bigc)