# Generated by Django 3.1.4 on 2021-01-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='actual_user',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='actual_user'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='borrow_wwid',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='borrow_wwid'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='po',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PO#'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='po_requestor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=' po_requestor'),
        ),
    ]
