# Generated by Django 5.0.7 on 2024-10-18 08:46

import ai_models.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ai_models", "0012_promptsmodel_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="promptsmodel",
            name="serial_number",
            field=ai_models.models.CustomIncrementalField(
                blank=True, default=0, editable=False
            ),
            preserve_default=False,
        ),
    ]
