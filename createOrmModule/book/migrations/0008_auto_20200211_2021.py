# Generated by Django 3.0.2 on 2020-02-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20200211_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_time']},
        ),
    ]