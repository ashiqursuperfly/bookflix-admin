from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, Reader, AuthorToBook, BookToGenre, FavoriteGenre, ReaderAuthorInteraction, ReaderBookInteraction


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'maturity_rating', 'isbn10', 'file_url']


@admin.register(AuthorToBook)
class AuthorToBookAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']


@admin.register(BookToGenre)
class GenreToBookAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']


@admin.register(FavoriteGenre)
class FavoriteGenreAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'genre_id']


@admin.register(ReaderBookInteraction)
class ReaderBookInteractionAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'user_id', 'current_page', 'is_favorite', 'is_on_my_list']


@admin.register(ReaderAuthorInteraction)
class ReaderAuthorInteractionAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'user_id', 'is_favorite']
