# Generated by Django 3.0.2 on 2020-02-11 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_article_removed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['create_time']},
        ),
        migrations.AlterModelTable(
            name='article',
            table='hello_world',
        ),
    ]
