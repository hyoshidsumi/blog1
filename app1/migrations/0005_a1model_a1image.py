# Generated by Django 5.0.1 on 2024-01-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_a1model'),
    ]

    operations = [
        migrations.AddField(
            model_name='a1model',
            name='a1image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]