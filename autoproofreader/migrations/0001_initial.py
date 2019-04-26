# Generated by Django 2.1.3 on 2019-04-25 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="AutoproofreaderResult",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "edition_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("name", models.TextField()),
                ("status", models.TextField()),
                ("skeleton_csv", models.TextField()),
                ("data", models.TextField(blank=True, null=True)),
                ("completion_time", models.DateTimeField(blank=True, null=True)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ComputeServer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("address", models.TextField()),
                (
                    "edition_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("diluvian_path", models.TextField()),
                ("results_directory", models.TextField()),
                ("environment_source_path", models.TextField(null=True)),
                (
                    "editor",
                    models.ForeignKey(
                        db_column="editor_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="compute_server_editor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConfigFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "edition_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("config", models.TextField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catmaid.Project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="DiluvianModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "edition_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("name", models.TextField()),
                ("model_source_path", models.TextField()),
                (
                    "config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoproofreader.ConfigFile",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catmaid.Project",
                    ),
                ),
                (
                    "server",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="autoproofreader.ComputeServer",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ImageVolumeConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "edition_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("name", models.TextField()),
                ("config", models.TextField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catmaid.Project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="config",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="autoproofreader.ConfigFile",
            ),
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="autoproofreader.DiluvianModel",
            ),
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="catmaid.Project"
            ),
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="skeleton",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="catmaid.ClassInstance"
            ),
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="autoproofreaderresult",
            name="volume",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catmaid.Volume",
            ),
        ),
    ]
