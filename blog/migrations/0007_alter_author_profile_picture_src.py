# Generated by Django 5.0.1 on 2024-01-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_author_profile_picture_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture_src',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
