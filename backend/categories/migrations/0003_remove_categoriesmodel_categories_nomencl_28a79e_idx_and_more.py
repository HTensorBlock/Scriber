# Generated by Django 5.0.7 on 2024-09-03 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_categoriesmodel_updater"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="categoriesmodel",
            name="categories_nomencl_28a79e_idx",
        ),
        migrations.AddField(
            model_name="categoriesmodel",
            name="deleted",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(
                fields=["nomenclature"], name="categories_nomencl_5ba644_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(fields=["code"], name="categories_code_a740e7_idx"),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(fields=["object"], name="categories_object_7d8b0f_idx"),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(
                fields=["condition"], name="categories_conditi_d389dc_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(fields=["norme"], name="categories_norme_15f3ba_idx"),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(
                fields=["fondement"], name="categories_fondeme_bcf461_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="categoriesmodel",
            index=models.Index(
                fields=["deleted"], name="categories_deleted_8a8689_idx"
            ),
        ),
    ]
