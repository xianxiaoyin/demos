# Generated by Django 3.1.4 on 2021-01-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historyuser',
            name='change_user',
        ),
        migrations.AddField(
            model_name='historyuser',
            name='actual_user',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change actual_user'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='bcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change username'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='borrow_wwid',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change borrow_wwid'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change category'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='comments',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change comments'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change location'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='project',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change project'),
        ),
        migrations.AddField(
            model_name='historyuser',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='change status'),
        ),
    ]
