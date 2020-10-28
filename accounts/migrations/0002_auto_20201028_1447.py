# Generated by Django 3.1.2 on 2020-10-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='住所'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tel',
            field=models.CharField(blank=True, max_length=30, verbose_name='電話番号'),
        ),
    ]
