# Generated by Django 3.0.3 on 2020-02-12 20:23

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
