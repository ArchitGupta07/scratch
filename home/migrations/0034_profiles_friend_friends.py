# Generated by Django 4.2.1 on 2023-05-28 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0033_projects_text_downloaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='friend',
            field=models.ManyToManyField(blank=True, default=None, related_name='friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profiles')),
                ('friend_s', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
