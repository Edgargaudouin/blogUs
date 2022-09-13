# Generated by Django 4.1 on 2022-09-13 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("appBlog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="avatares"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="commenter_id",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="publication",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="user", name="password", field=models.CharField(max_length=35),
        ),
    ]