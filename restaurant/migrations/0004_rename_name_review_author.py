# Generated by Django 5.0.4 on 2024-05-01 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Name',
            new_name='author',
        ),
    ]