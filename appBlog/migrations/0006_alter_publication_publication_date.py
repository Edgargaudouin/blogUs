# Generated by Django 4.1 on 2022-09-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0005_remove_publication_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]