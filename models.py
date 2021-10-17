# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aircompany(models.Model):
    companyid = models.IntegerField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admin = models.CharField(db_column='Admin', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AirCompany'


class Airport(models.Model):
    airportid = models.AutoField(db_column='AirportID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airportname = models.CharField(db_column='AirportName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Airport'


class Flight(models.Model):
    flightid = models.CharField(db_column='FlightID', primary_key=True, max_length=30)  # Field name made lowercase.
    planeid = models.IntegerField(db_column='PlaneID', blank=True, null=True)  # Field name made lowercase.
    flightname = models.CharField(db_column='FlightName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utime = models.CharField(db_column='UTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtime = models.CharField(db_column='DTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdelay = models.CharField(db_column='IsDelay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seatleft = models.IntegerField(db_column='SeatLeft', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'


class Plane(models.Model):
    planeid = models.AutoField(db_column='PlaneID', primary_key=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    planemodel = models.CharField(db_column='PlaneModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    npeople = models.IntegerField(db_column='NPeople', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plane'



class Ticket(models.Model):
    ticketid = models.AutoField(db_column='TicketID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flightid = models.CharField(db_column='FlightID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    airportid = models.CharField(db_column='AirportID', max_length=11, blank=True, null=True)   # Field name made lowercase.
    money = models.CharField(db_column='Money', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ticket'

class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userage = models.CharField(db_column='UserAge', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useridentity = models.CharField(db_column='UserIdentity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isvip = models.PositiveIntegerField(db_column='isVip')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
