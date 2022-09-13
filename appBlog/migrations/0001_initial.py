# Generated by Django 4.1 on 2022-09-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("commenter_id", models.TextField(max_length=300)),
                ("commenter_name", models.CharField(max_length=200)),
                ("comment_body", models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=60)),
                ("caption", models.CharField(max_length=60)),
                ("category", models.CharField(max_length=20)),
                ("sub_category", models.CharField(max_length=20)),
                ("author", models.CharField(max_length=25)),
                ("body", models.TextField(max_length=9600)),
                ("publication_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("lastname", models.CharField(max_length=20)),
                ("nickname", models.CharField(max_length=20, unique=True)),
                ("password", models.TextField(max_length=35)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("birth_date", models.DateField()),
            ],
        ),
    ]
