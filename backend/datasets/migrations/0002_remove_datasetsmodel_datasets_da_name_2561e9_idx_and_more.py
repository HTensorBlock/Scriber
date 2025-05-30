# Generated by Django 5.0.7 on 2024-09-04 10:26

import datasets.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "categories",
            "0003_remove_categoriesmodel_categories_nomencl_28a79e_idx_and_more",
        ),
        ("datasets", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="datasetsmodel",
            name="datasets_da_name_2561e9_idx",
        ),
        migrations.AddField(
            model_name="datasetsmodel",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="datasetsmodel",
            name="serial_number",
            field=datasets.models.CustomIncrementalField(
                blank=True, editable=False
            ),
        ),
        migrations.AddIndex(
            model_name="datasetsmodel",
            index=models.Index(fields=["name"], name="datasets_da_name_c555b6_idx"),
        ),
        migrations.AddIndex(
            model_name="datasetsmodel",
            index=models.Index(
                fields=["categorie"], name="datasets_da_categor_c608f4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="datasetsmodel",
            index=models.Index(
                fields=["deleted"], name="datasets_da_deleted_9855b3_idx"
            ),
        ),
    ]
