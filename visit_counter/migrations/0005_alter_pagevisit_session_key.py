# Generated by Django 4.1.7 on 2023-03-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit_counter', '0004_remove_pagevisit_session_pagevisit_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagevisit',
            name='session_key',
            field=models.CharField(max_length=350),
        ),
    ]
