# Generated by Django 3.1.5 on 2021-01-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20210127_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='comments',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='comments'),
        ),
    ]