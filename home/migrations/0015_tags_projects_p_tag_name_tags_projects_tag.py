# Generated by Django 4.2.1 on 2023-05-25 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_pcomments_pname'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags_projects',
            name='p_tag_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projects'),
        ),
        migrations.AddField(
            model_name='tags_projects',
            name='tag',
            field=models.CharField(default='None', max_length=100),
        ),
    ]