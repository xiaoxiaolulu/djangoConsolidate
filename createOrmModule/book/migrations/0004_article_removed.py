# Generated by Django 3.0.2 on 2020-02-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='removed',
            field=models.BooleanField(default=1),
        ),
    ]
