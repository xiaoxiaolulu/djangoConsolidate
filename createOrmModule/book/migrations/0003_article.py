# Generated by Django 3.0.2 on 2020-02-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
