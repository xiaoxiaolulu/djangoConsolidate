# Generated by Django 3.0.2 on 2020-02-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200211_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('article', models.ManyToManyField(to='article.Article')),
            ],
        ),
    ]
