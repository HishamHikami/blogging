# Generated by Django 5.0.6 on 2024-05-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_customtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
