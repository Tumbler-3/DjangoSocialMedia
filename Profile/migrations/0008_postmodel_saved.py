# Generated by Django 5.0 on 2024-01-09 16:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_alter_postmodel_responsed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='caved_by', to=settings.AUTH_USER_MODEL),
        ),
    ]