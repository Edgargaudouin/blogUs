# Generated by Django 4.1 on 2022-09-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0011_remove_category_publications_publication_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
    ]
