# Generated by Django 4.2.2 on 2024-03-02 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0015_cohorte_delted_cohorte_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cohorte',
            name='user',
        ),
        migrations.AddField(
            model_name='cohorte',
            name='teacher',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('is_profesor', True)), null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
