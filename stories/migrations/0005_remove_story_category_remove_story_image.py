# Generated by Django 4.2 on 2024-06-25 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_alter_story_options_alter_story_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='category',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
    ]
