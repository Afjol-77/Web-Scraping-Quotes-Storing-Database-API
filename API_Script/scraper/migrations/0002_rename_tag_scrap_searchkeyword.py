# Generated by Django 5.0.6 on 2024-05-17 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrap',
            old_name='tag',
            new_name='searchKeyword',
        ),
    ]
