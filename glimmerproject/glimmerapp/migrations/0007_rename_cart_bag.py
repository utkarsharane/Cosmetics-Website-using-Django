# Generated by Django 5.0 on 2023-12-19 05:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("glimmerapp", "0006_cart_userid"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cart",
            new_name="Bag",
        ),
    ]
