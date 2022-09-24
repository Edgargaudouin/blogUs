# Generated by Django 4.1 on 2022-09-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0010_remove_comment_author_comment_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='publications',
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.CharField(default='sin categoria!', max_length=60),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='Sin categoria', max_length=200),
        ),
    ]
