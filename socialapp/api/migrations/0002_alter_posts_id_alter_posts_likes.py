# Generated by Django 4.1.5 on 2023-01-31 13:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="posts",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="blogpost_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
