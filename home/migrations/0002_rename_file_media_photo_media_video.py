# Generated by Django 5.1.1 on 2024-11-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='file',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='media',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
