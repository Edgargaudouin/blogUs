# Generated by Django 4.1 on 2022-10-05 00:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appBlog", "0018_alter_publication_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]