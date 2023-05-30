# Generated by Django 4.2.1 on 2023-05-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_profiles_image_alter_projects_p_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(default=None, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='p_image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]