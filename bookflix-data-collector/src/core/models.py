from django.db import models
from django.utils import timezone


class Genre(models.Model):

    name = models.CharField(max_length=256)

    date_added = models.DateField(editable=False)
    date_modified = models.DateField(editable=True)

    class Meta:
        verbose_name_plural = "Genres"

    def save(self, *args, **kwargs):
        if self.id:
            self.date_modified = timezone.now()
        else:
            self.date_added = timezone.now()
            self.date_modified = timezone.now()

        super(Genre, self).save(*args, **kwargs)


class Author(models.Model):

    name = models.CharField(max_length=256)

    birthYear = models.IntegerField(null=True, blank=True)
    deathYear = models.IntegerField(null=True, blank=True)

    date_added = models.DateField(editable=False)
    date_modified = models.DateField(editable=True)

    class Meta:
        verbose_name_plural = "Authors"

    def save(self, *args, **kwargs):
        if self.id:
            self.date_modified = timezone.now()
        else:
            self.date_added = timezone.now()
            self.date_modified = timezone.now()

        super(Author, self).save(*args, **kwargs)


class Book(models.Model):

    S3_BOOKS = "books"
    S3_BOOK_COVERS = "book-covers"

    fileUrl = models.FileField(upload_to=S3_BOOKS)
    coverImgUrl = models.FileField(upload_to=S3_BOOK_COVERS, null=True, blank=True)

    title = models.CharField(max_length=512)

    fileType = models.CharField(max_length=32, null=True, blank=True)
    language = models.CharField(max_length=24, null=True, blank=True)
    copyright = models.BooleanField(default=False)

    genres = models.ManyToManyField(Genre, related_name="books", blank=True)
    authors = models.ManyToManyField(Author, related_name="books", blank=True)

    date_added = models.DateField(editable=False)
    date_modified = models.DateField(editable=True)

    class Meta:
        verbose_name_plural = "Books"

    def save(self, *args, **kwargs):
        if self.id:
            self.date_modified = timezone.now()
        else:
            self.date_added = timezone.now()
            self.date_modified = timezone.now()

        super(Book, self).save(*args, **kwargs)
