# Generated by Django 2.1.1 on 2018-09-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20180924_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='hashtags',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='Hashtags'),
        ),
        migrations.AlterField(
            model_name='order',
            name='similar_users',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='Similar Users'),
        ),
    ]
