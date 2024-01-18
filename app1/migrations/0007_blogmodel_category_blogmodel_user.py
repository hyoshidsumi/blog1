# Generated by Django 5.0.1 on 2024-01-17 02:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_blogmodel_cdate_alter_blogmodel_udate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('todo', 'Todo'), ('blog', 'Blog'), ('else', 'Else')], default='Todo', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
