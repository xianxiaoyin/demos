# Generated by Django 3.1.5 on 2021-01-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20210120_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='bcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Barcode'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='sn',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='status name'),
        ),
    ]
