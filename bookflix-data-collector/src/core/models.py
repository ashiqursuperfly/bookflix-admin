# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reader(models.Model):
    password = models.TextField()
    created_at = models.DateTimeField(db_column='createdAt')
    username = models.TextField(unique=True)
    name = models.TextField()

    class Meta:
        db_table = 'User'


class Genre(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'Genre'


class Author(models.Model):
    name = models.TextField(unique=True)
    birth_year = models.IntegerField(db_column='birthYear', blank=True, null=True)
    death_year = models.IntegerField(db_column='deathYear', blank=True, null=True)
    created_at = models.DateTimeField(db_column='createdAt')

    class Meta:
        db_table = 'Author'


class Book(models.Model):
    created_at = models.DateTimeField(db_column='createdAt')
    title = models.TextField(unique=True)
    copyright = models.BooleanField()
    language = models.TextField()
    updated_at = models.DateTimeField(db_column='updatedAt')
    file_url = models.TextField(db_column='fileUrl', unique=True)
    file_type = models.TextField(db_column='fileType')
    cover_image_url = models.TextField(db_column='coverImageUrl', blank=True, null=True)

    class Meta:
        db_table = 'Book'


class FavoriteGenre(models.Model):
    genre_id = models.ForeignKey(Genre, models.CASCADE, db_column='genreId')
    user_id = models.ForeignKey(Reader, models.CASCADE, db_column='userId')
    type = models.TextField()  # This field type is a guess.
    relevance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FavoriteGenre'
        unique_together = (('genre_id', 'user_id'),)


class ReaderBookInteraction(models.Model):
    book_id = models.ForeignKey(Book, models.CASCADE, db_column='bookId')
    user_id = models.ForeignKey(Reader, models.CASCADE, db_column='userId')
    current_page = models.IntegerField(db_column='currentPage')
    is_finished_reading = models.BooleanField(db_column='isFinishedReading')
    start_date = models.DateTimeField(db_column='startDate')
    last_update = models.DateTimeField(db_column='lastUpdate')
    is_favorite = models.BooleanField(db_column='isFavorite')
    is_on_my_list = models.BooleanField(db_column='isOnMyList')

    class Meta:
        managed = False
        db_table = 'UserBookInteraction'
        unique_together = (('book_id', 'user_id'),)


class AuthorToBook(models.Model):
    a = models.ForeignKey(Author, models.CASCADE, db_column='A')
    b = models.ForeignKey(Book, models.CASCADE, db_column='B')

    class Meta:
        managed = False
        db_table = '_AuthorToBook'
        unique_together = (('a', 'b'),)


class BookToGenre(models.Model):
    a = models.ForeignKey(Book, models.CASCADE, db_column='A')
    b = models.ForeignKey(Genre, models.CASCADE, db_column='B')

    class Meta:
        managed = False
        db_table = '_BookToGenre'
        unique_together = (('a', 'b'),)


class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'
