# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplyTask(models.Model):
    submitter = models.ForeignKey('Submitter', models.DO_NOTHING, primary_key=True)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    approved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apply_task'
        unique_together = (('submitter', 'task'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class MyAdmin(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'my_admin'


class ParsedData(models.Model):
    parsed_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    submitter = models.ForeignKey('Submitter', models.DO_NOTHING)
    rater = models.ForeignKey('Rater', models.DO_NOTHING)
    raw_data_seq_file = models.ForeignKey('RawDataSeqFile', models.DO_NOTHING, db_column='raw_data_seq_file')
    total_tuple_num = models.IntegerField(blank=True, null=True)
    duplicate_tuple_num = models.IntegerField(blank=True, null=True)
    column_null_ratio = models.FloatField(blank=True, null=True)
    quantity_score = models.IntegerField(blank=True, null=True)
    quality_score = models.IntegerField(blank=True, null=True)
    evaluated = models.IntegerField()
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'parsed_data'


class Rater(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rater'


class RawDataSeqFile(models.Model):
    seqnumber = models.AutoField(primary_key=True)
    submitter = models.ForeignKey('Submitter', models.DO_NOTHING)
    raw_data_type = models.ForeignKey('RawDataType', models.DO_NOTHING, db_column='raw_data_type')
    term = models.DateField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raw_data_seq_file'


class RawDataType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=30)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    admin = models.ForeignKey(MyAdmin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'raw_data_type'


class Submitter(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, primary_key=True)
    grade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'submitter'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=100)
    mincycle = models.IntegerField()
    admin = models.ForeignKey(MyAdmin, models.DO_NOTHING, db_column='admin')

    class Meta:
        managed = False
        db_table = 'task'


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=10)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=12)  # Field name made lowercase.
    lname = models.CharField(max_length=15)
    fname = models.CharField(max_length=30)
    birthdate = models.DateField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user_profile'
