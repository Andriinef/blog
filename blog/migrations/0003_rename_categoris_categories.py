# Generated by Django 4.1.1 on 2022-10-04 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content_alter_post_reply'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoris',
            new_name='Categories',
        ),
    ]
