# Generated by Django 4.2 on 2024-06-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_story_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]