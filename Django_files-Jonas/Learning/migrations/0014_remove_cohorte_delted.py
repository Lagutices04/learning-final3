# Generated by Django 4.2.2 on 2024-03-01 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0013_rename_deleted_cohorte_delted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cohorte',
            name='delted',
        ),
    ]
