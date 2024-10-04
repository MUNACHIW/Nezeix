# Generated by Django 5.1.1 on 2024-10-04 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_remove_post_image_name_post_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=120)),
                ("user_email", models.EmailField(max_length=254)),
                ("text", models.TextField(max_length=400)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="Blog.post",
                    ),
                ),
            ],
        ),
    ]
