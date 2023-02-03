from django.contrib import admin
from .models import Book, InfoBook, Finder


admin.site.register(Book)
admin.site.register(InfoBook)
admin.site.register(Finder)

# Register your models here.
