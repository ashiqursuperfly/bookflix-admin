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

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'Genre'

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.TextField(unique=True)
    birth_year = models.IntegerField(db_column='birthYear', blank=True, null=True)
    death_year = models.IntegerField(db_column='deathYear', blank=True, null=True)
    created_at = models.DateTimeField(db_column='createdAt')

    class Meta:
        db_table = 'Author'

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    created_at = models.DateTimeField(db_column='createdAt')
    title = models.TextField(unique=True)
    copyright = models.BooleanField()
    language = models.TextField()
    updated_at = models.DateTimeField(db_column='updatedAt')
    description = models.TextField(blank=True, null=True)
    file_url = models.TextField(db_column='fileUrl', unique=True)
    file_type = models.TextField(db_column='fileType')
    cover_image_url = models.TextField(db_column='coverImageUrl', blank=True, null=True)
    isbn10 = models.TextField(unique=True, blank=True, null=True)
    isbn13 = models.TextField(unique=True, blank=True, null=True)
    maturity_rating = models.TextField(db_column='maturityRating', blank=True, null=True)
    rating = models.DecimalField(max_digits=65, decimal_places=30, blank=True, null=True)
    year_published = models.TextField(db_column='yearPublished', blank=True, null=True)

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return str(self.title)


class FavoriteGenre(models.Model):
    genre_id = models.ForeignKey(Genre, models.CASCADE, db_column='genreId')
    user_id = models.ForeignKey(Reader, models.CASCADE, db_column='userId')
    type = models.TextField()  # TODO: This field type is a guess.
    relevance = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'FavoriteGenre'
        unique_together = ('genre_id', 'user_id')

    def __str__(self):
        return '{genre: ' + str(self.genre_id) + ", user: " + str(self.user_id) + "}"


class AuthorToBook(models.Model):
    author = models.ForeignKey(Author, models.CASCADE, db_column='A')
    book = models.ForeignKey(Book, models.CASCADE, db_column='B')

    class Meta:
        db_table = '_AuthorToBook'
        unique_together = ('author', 'book')

    def __str__(self):
        return '{author: ' + str(self.author) + ", book: " + str(self.book) + "}"


class BookToGenre(models.Model):
    author = models.ForeignKey(Book, models.CASCADE, db_column='A')
    book = models.ForeignKey(Genre, models.CASCADE, db_column='B')

    class Meta:
        db_table = '_BookToGenre'
        unique_together = ('author', 'book')

    def __str__(self):
        return '{author: ' + str(self.author) + ", book: " + str(self.book) + "}"


class ReaderBookInteraction(models.Model):
    book_id = models.ForeignKey(Book, models.CASCADE, db_column='bookId')
    user_id = models.ForeignKey(Reader, models.CASCADE, db_column='userId')
    is_finished_reading = models.BooleanField(db_column='isFinishedReading')
    start_date = models.DateTimeField(db_column='startDate')
    last_update = models.DateTimeField(db_column='lastUpdate')
    is_favorite = models.BooleanField(db_column='isFavorite')
    is_on_my_list = models.BooleanField(db_column='isOnMyList')

    class Meta:
        db_table = 'UserBookInteraction'
        unique_together = ('book_id', 'user_id')

    def __str__(self):
        return '{book: ' + str(self.book_id) + ", user: " + str(self.user_id) + ", page" + "}"


class ReaderAuthorInteraction(models.Model):
    user_id = models.ForeignKey(Reader, models.CASCADE, db_column='userId')
    author_id = models.ForeignKey(Author, models.CASCADE, db_column='authorId')
    is_favorite = models.BooleanField(db_column='isFavorite')

    class Meta:
        db_table = 'UserAuthorInteraction'
        unique_together = ('author_id', 'user_id')

    def __str__(self):
        return '{user: ' + str(self.user_id) + ", author: " + str(self.author_id) + ", is_favorite" + str(self.is_favorite) + "}"


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
