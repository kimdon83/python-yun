# Generated by Django 4.1 on 2023-02-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research", "0007_publication_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="abstract",
            field=models.CharField(default="", max_length=2000),
        ),
    ]
