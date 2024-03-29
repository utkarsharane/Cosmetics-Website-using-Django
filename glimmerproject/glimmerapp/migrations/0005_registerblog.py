# Generated by Django 5.0 on 2023-12-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("glimmerapp", "0004_remove_wishlist_qty"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegisterBlog",
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
                ("photo", models.ImageField(default="none", upload_to="images")),
                ("title", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
            ],
        ),
    ]
