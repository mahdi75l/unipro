# Generated by Django 3.0.3 on 2020-02-15 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20200215_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='guid',
            name='ceated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guid',
            name='address',
            field=models.FileField(blank=True, null=True, upload_to='FileGuid/'),
        ),
    ]