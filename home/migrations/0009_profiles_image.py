# Generated by Django 4.2.1 on 2023-05-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_tags_projects_remove_projects_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default='None', upload_to='static/images'),
        ),
    ]