# Generated by Django 5.0.7 on 2024-10-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("decisions", "0002_datasetsdecisionsmodel_deleted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rawdecisionsmodel",
            name="j_rg",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
