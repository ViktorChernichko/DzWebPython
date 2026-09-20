from django.apps import apps as global_apps
from django.contrib.auth.management import create_permissions
from django.db import migrations


def create_groups(apps, schema_editor):
    app_config = global_apps.get_app_config('dz14')
    create_permissions(app_config, verbosity=0)

    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    book_ct = ContentType.objects.get(app_label='dz14', model='book')
    reader_ct = ContentType.objects.get(app_label='dz14', model='reader')

    view_codenames = ['view_book', 'view_reader']
    full_codenames = [
        'add_book', 'change_book', 'delete_book', 'view_book',
        'add_reader', 'change_reader', 'delete_reader', 'view_reader',
    ]

    view_permissions = Permission.objects.filter(
        content_type__in=[book_ct, reader_ct], codename__in=view_codenames
    )
    full_permissions = Permission.objects.filter(
        content_type__in=[book_ct, reader_ct], codename__in=full_codenames
    )

    librarians, _ = Group.objects.get_or_create(name='Librarians')
    librarians.permissions.set(view_permissions)

    administrators, _ = Group.objects.get_or_create(name='Administrators')
    administrators.permissions.set(full_permissions)


def remove_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Librarians', 'Administrators']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dz14', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups, remove_groups),
    ]
