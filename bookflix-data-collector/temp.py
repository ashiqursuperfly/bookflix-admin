# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Author(models.Model):
#     name = models.TextField(unique=True)
#     birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
#     deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'Author'
#
#
# class Book(models.Model):
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     title = models.TextField(unique=True)
#     copyright = models.BooleanField()
#     language = models.TextField()
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     fileurl = models.TextField(db_column='fileUrl', unique=True)  # Field name made lowercase.
#     filetype = models.TextField(db_column='fileType')  # Field name made lowercase.
#     coverimageurl = models.TextField(db_column='coverImageUrl', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'Book'
#
#
# class Favoritegenre(models.Model):
#     genreid = models.ForeignKey('Genre', models.DO_NOTHING, db_column='genreId')  # Field name made lowercase.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
#     type = models.TextField()  # This field type is a guess.
#     relevance = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'FavoriteGenre'
#         unique_together = (('genreid', 'userid'),)
#
#
# class Genre(models.Model):
#     name = models.TextField(unique=True)
#
#     class Meta:
#         db_table = 'Genre'
#
#
# class User(models.Model):
#     password = models.TextField()
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     username = models.TextField(unique=True)
#     name = models.TextField()
#
#     class Meta:
#         db_table = 'User'
#
#
# class Userbookinteraction(models.Model):
#     bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bookId')  # Field name made lowercase.
#     userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
#     currentpage = models.IntegerField(db_column='currentPage')  # Field name made lowercase.
#     isfinishedreading = models.BooleanField(db_column='isFinishedReading')  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
#     lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
#     isfavorite = models.BooleanField(db_column='isFavorite')  # Field name made lowercase.
#     isonmylist = models.BooleanField(db_column='isOnMyList')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'UserBookInteraction'
#         unique_together = (('bookid', 'userid'),)
#
#
# class Authortobook(models.Model):
#     a = models.ForeignKey(Author, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
#     b = models.ForeignKey(Book, models.DO_NOTHING, db_column='B')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = '_AuthorToBook'
#         unique_together = (('a', 'b'),)
#
#
# class Booktogenre(models.Model):
#     a = models.ForeignKey(Book, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
#     b = models.ForeignKey(Genre, models.DO_NOTHING, db_column='B')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = '_BookToGenre'
#         unique_together = (('a', 'b'),)
#
#
# class PrismaMigrations(models.Model):
#     id = models.CharField(primary_key=True, max_length=36)
#     checksum = models.CharField(max_length=64)
#     finished_at = models.DateTimeField(blank=True, null=True)
#     migration_name = models.CharField(max_length=255)
#     logs = models.TextField(blank=True, null=True)
#     rolled_back_at = models.DateTimeField(blank=True, null=True)
#     started_at = models.DateTimeField()
#     applied_steps_count = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = '_prisma_migrations'
