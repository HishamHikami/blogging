# Generated by Django 5.0.6 on 2024-05-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_customtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtag',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
