# Generated by Django 4.2.1 on 2023-05-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_profiles_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='likes',
        ),
        migrations.AddField(
            model_name='projects',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
