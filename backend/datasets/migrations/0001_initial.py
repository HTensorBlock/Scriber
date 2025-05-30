# Generated by Django 5.0.7 on 2024-08-29 14:49

import categories.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DatasetsModel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "serial_number",
                    categories.models.CustomIncrementalField(
                        blank=True, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", max_length=4096, null=True
                    ),
                ),
                ("size", models.PositiveIntegerField(blank=True, default=0, null=True)),
                (
                    "annotated_decisions",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "categorie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="dataset_categorie",
                        to="categories.categoriesmodel",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="datasets_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["serial_number"],
            },
        ),
        migrations.CreateModel(
            name="DatasetsLabelsModel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="dataset",
                        to="datasets.datasetsmodel",
                    ),
                ),
            ],
            options={
                "db_table": "datasets_labels",
            },
        ),
        migrations.CreateModel(
            name="Labels",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", max_length=4096, null=True
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, default="#f0f0f0", max_length=7, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="labels_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "labels",
                "ordering": ["label"],
            },
        ),
        migrations.AddField(
            model_name="datasetsmodel",
            name="labels",
            field=models.ManyToManyField(
                blank=True,
                related_name="labels",
                through="datasets.DatasetsLabelsModel",
                to="datasets.labels",
            ),
        ),
        migrations.AddField(
            model_name="datasetslabelsmodel",
            name="label",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="label_id",
                to="datasets.labels",
            ),
        ),
        migrations.AddIndex(
            model_name="labels",
            index=models.Index(fields=["label"], name="labels_label_bf9bc0_idx"),
        ),
        migrations.AddIndex(
            model_name="datasetsmodel",
            index=models.Index(
                fields=["name", "categorie"], name="datasets_da_name_2561e9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="datasetslabelsmodel",
            index=models.Index(
                fields=["dataset"], name="datasets_la_dataset_7ae5ac_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="datasetslabelsmodel",
            constraint=models.UniqueConstraint(
                fields=("dataset", "label"), name="unique_train_dataset_label"
            ),
        ),
    ]
