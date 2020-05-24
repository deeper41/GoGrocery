# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulo(models.Model):
    aritculo_id = models.AutoField(primary_key=True)
    subcategoria = models.ForeignKey('Subcategoria', models.DO_NOTHING)
    aritculo_nombre = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    articulo_url = models.TextField()
    activo = models.IntegerField()
    ejemplos_existentes = models.IntegerField()
    fecha_registro_articulo = models.DateField()
    tienda = models.ForeignKey('Tienda', models.DO_NOTHING)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Articulo'


class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=125)
    imagen = models.TextField()
    subcategoria_cantidad = models.IntegerField(db_column='subcategoria-cantidad')  # Field renamed to remove unsuitable characters.
    fecha_registro_categoria = models.DateField(blank=True, null=True)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Categoria'


class Fragmento(models.Model):
    fragmento_id = models.AutoField(primary_key=True)
    lista = models.ForeignKey('Lista', models.DO_NOTHING)
    aritculo = models.ForeignKey(Articulo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Fragmento'


class Lista(models.Model):
    lista_id = models.AutoField(primary_key=True)
    lista_fecha = models.DateField()
    nombre = models.TextField()
    precio_total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Lista'


class Subcategoria(models.Model):
    subcategoria_id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    imagen = models.TextField()
    fecha_registro_subcategoria = models.DateField()
    id_nombre = models.CharField(max_length=45)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Subcategoria'


class Tienda(models.Model):
    tienda_id = models.AutoField(primary_key=True)
    tienda_nombre = models.CharField(max_length=50)
    tienda_url = models.TextField()
    fecha_registro_tienda = models.DateField()
    id_nombre_tie = models.CharField(max_length=45)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Tienda'


class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    contrasenia = models.CharField(max_length=62)
    nickname = models.CharField(max_length=25)
    fecha_ultimo_login = models.DateField()
    fecha_registro_usuario = models.DateField()
    activo = models.IntegerField()
    admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    action_flag = models.PositiveSmallIntegerField()
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
