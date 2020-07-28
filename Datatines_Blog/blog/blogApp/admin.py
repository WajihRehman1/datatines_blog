from django.contrib import admin
from .models import post,Catagory,Author,comment
# Register your models here.
admin.site.register(post)
admin.site.register(Catagory)
admin.site.register(Author)
admin.site.register(comment)