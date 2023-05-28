# Generated by Django 4.2.1 on 2023-05-27 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0024_remove_projects_likes_lovers_value_projects_liked_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pv_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
                ('viewer', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]