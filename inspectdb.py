postgres d3un8idklth2st
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    name = models.TextField(unique=True)
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Author'


class Book(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    title = models.TextField(unique=True)
    copyright = models.BooleanField()
    language = models.TextField()
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    fileurl = models.TextField(db_column='fileUrl', unique=True)  # Field name made lowercase.
    filetype = models.TextField(db_column='fileType')  # Field name made lowercase.
    coverimageurl = models.TextField(db_column='coverImageUrl', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    isbn10 = models.TextField(unique=True, blank=True, null=True)
    isbn13 = models.TextField(unique=True, blank=True, null=True)
    maturityrating = models.TextField(db_column='maturityRating', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=65, decimal_places=30, blank=True, null=True)
    yearpublished = models.TextField(db_column='yearPublished', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book'


class Favoritegenre(models.Model):
    genreid = models.ForeignKey('Genre', models.DO_NOTHING, db_column='genreId')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    relevance = models.IntegerField(blank=True, null=True)
    type = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'FavoriteGenre'
        unique_together = (('genreid', 'userid'),)


class Genre(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'Genre'


class User(models.Model):
    password = models.TextField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    name = models.TextField()
    username = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'User'


class Userauthorinteraction(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    authorid = models.ForeignKey(Author, models.DO_NOTHING, db_column='authorId')  # Field name made lowercase.
    isfavorite = models.BooleanField(db_column='isFavorite')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserAuthorInteraction'
        unique_together = (('authorid', 'userid'),)


class Userbookinteraction(models.Model):
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bookId')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    currentpage = models.IntegerField(db_column='currentPage')  # Field name made lowercase.
    isfinishedreading = models.BooleanField(db_column='isFinishedReading')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    isfavorite = models.BooleanField(db_column='isFavorite')  # Field name made lowercase.
    isonmylist = models.BooleanField(db_column='isOnMyList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserBookInteraction'
        unique_together = (('bookid', 'userid'),)


class Authortobook(models.Model):
    a = models.ForeignKey(Author, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
    b = models.ForeignKey(Book, models.DO_NOTHING, db_column='B')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_AuthorToBook'
        unique_together = (('a', 'b'),)


class Booktogenre(models.Model):
    a = models.ForeignKey(Book, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
    b = models.ForeignKey(Genre, models.DO_NOTHING, db_column='B')  # Field name made lowercase.

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


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.BooleanField()
    title = models.CharField(max_length=50)
    title_visible = models.BooleanField()
    logo = models.CharField(max_length=100)
    logo_visible = models.BooleanField()
    css_header_background_color = models.CharField(max_length=10)
    title_color = models.CharField(max_length=10)
    css_header_text_color = models.CharField(max_length=10)
    css_header_link_color = models.CharField(max_length=10)
    css_header_link_hover_color = models.CharField(max_length=10)
    css_module_background_color = models.CharField(max_length=10)
    css_module_text_color = models.CharField(max_length=10)
    css_module_link_color = models.CharField(max_length=10)
    css_module_link_hover_color = models.CharField(max_length=10)
    css_module_rounded_corners = models.BooleanField()
    css_generic_link_color = models.CharField(max_length=10)
    css_generic_link_hover_color = models.CharField(max_length=10)
    css_save_button_background_color = models.CharField(max_length=10)
    css_save_button_background_hover_color = models.CharField(max_length=10)
    css_save_button_text_color = models.CharField(max_length=10)
    css_delete_button_background_color = models.CharField(max_length=10)
    css_delete_button_background_hover_color = models.CharField(max_length=10)
    css_delete_button_text_color = models.CharField(max_length=10)
    css = models.TextField()
    list_filter_dropdown = models.BooleanField()
    related_modal_active = models.BooleanField()
    related_modal_background_color = models.CharField(max_length=10)
    related_modal_rounded_corners = models.BooleanField()
    logo_color = models.CharField(max_length=10)
    recent_actions_visible = models.BooleanField()
    favicon = models.CharField(max_length=100)
    related_modal_background_opacity = models.CharField(max_length=5)
    env_name = models.CharField(max_length=50)
    env_visible_in_header = models.BooleanField()
    env_color = models.CharField(max_length=10)
    env_visible_in_favicon = models.BooleanField()
    related_modal_close_button_visible = models.BooleanField()
    language_chooser_active = models.BooleanField()
    language_chooser_display = models.CharField(max_length=10)
    list_filter_sticky = models.BooleanField()
    form_pagination_sticky = models.BooleanField()
    form_submit_sticky = models.BooleanField()
    css_module_background_selected_color = models.CharField(max_length=10)
    css_module_link_selected_color = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
