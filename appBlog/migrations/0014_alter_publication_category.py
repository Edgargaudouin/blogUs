# Generated by Django 4.1 on 2022-09-28 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0013_alter_publication_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBlog.category'),
        ),
    ]