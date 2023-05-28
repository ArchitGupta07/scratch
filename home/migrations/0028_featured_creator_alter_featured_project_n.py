# Generated by Django 4.2.1 on 2023-05-28 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='creator',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='home.projects'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='project_n',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_n', to='home.projects'),
        ),
    ]