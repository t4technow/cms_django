# Generated by Django 4.1.7 on 2023-02-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_author_request_date_author_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
