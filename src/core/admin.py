from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Author, Genre, Book, Reader, AuthorToBook, BookToGenre, FavoriteGenre, ReaderAuthorInteraction, ReaderBookInteraction


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_at', admin.DateFieldListFilter),
    )

    search_fields = ['name']
    list_display = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_per_page = 6
    list_max_show_all = 10

    search_fields = ['title']

    @staticmethod
    def date_published(obj):
        if obj.year_published:
            return str(obj.year_published)[0:3]
        return "n/a"

    list_filter = (
        'maturity_rating',
        'year_published',
        ('updated_at', admin.DateFieldListFilter)
    )

    @staticmethod
    def score(obj):
        if obj.rating:
            rating = float(obj.rating)
            return rating
        else:
            return "n/a"

    @staticmethod
    def cover_image(obj):
        img_url = f"https://bookflix-dev.s3.ap-southeast-1.amazonaws.com/{obj.cover_image_url}"
        img = '<img src="{0}" style="width: 120px; height:150px;" />'.format(img_url)
        return format_html(img)

    list_display = ['cover_image', 'title', 'maturity_rating', 'isbn10', 'score', 'date_published']


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
