# Generated by Django 5.0.3 on 2024-05-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0002_rename_slug_articlepage_subtilte_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="subtilte",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="subtilte",
            field=models.CharField(max_length=200),
        ),
    ]
