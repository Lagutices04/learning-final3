# Generated by Django 4.2.2 on 2024-03-03 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0016_remove_cohorte_user_cohorte_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cohorte',
            name='codigoCoh',
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Learning.cohorte', verbose_name='Curso')),
                ('student', models.ForeignKey(blank=True, limit_choices_to=models.Q(('is_Estudiante', True)), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students_registration', to=settings.AUTH_USER_MODEL, verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Inscripcion',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
    ]
