# Generated by Django 4.2.1 on 2023-05-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_tags_projects_p_tag_name_tags_projects_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.URLField(default='None', null=True),
        ),
    ]