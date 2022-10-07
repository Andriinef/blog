# Generated by Django 4.1.1 on 2022-10-07 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_categoris_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Публікація'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcategory', to='blog.categories', verbose_name='Категорії'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, unique_for_date='publish', verbose_name='URL'),
        ),
    ]
