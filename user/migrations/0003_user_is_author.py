# Generated by Django 4.1.7 on 2023-03-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_following_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=True),
        ),
    ]
