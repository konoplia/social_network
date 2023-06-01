# Generated by Django 4.2.1 on 2023-06-01 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.CharField(max_length=2000)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("like", models.BooleanField(default=False)),
                ("like_date", models.DateField(blank=True, null=True)),
                ("dislike", models.BooleanField(default=False)),
                ("dislike_date", models.DateField(blank=True, null=True)),
                (
                    "blog_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reaction",
                        to="blog.blogpost",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="reaction",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
