from django.contrib import admin
from .models import Post
from .models import Students,Teachers

admin.site.register(Post)
admin.site.register(Students)
admin.site.register(Teachers)