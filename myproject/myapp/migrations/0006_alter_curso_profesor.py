# Generated by Django 4.2.4 on 2023-09-05 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_curso_profesor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="profesor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cursos",
                to="myapp.profesor",
            ),
        ),
    ]
