from django.contrib import admin


# Register your models here.
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'fileUrl', 'fileType']
