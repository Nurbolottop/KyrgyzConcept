# Generated by Django 4.2.6 on 2023-10-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='youtube',
        ),
        migrations.AddField(
            model_name='settings',
            name='tripadvisor',
            field=models.URLField(blank=True, null=True, verbose_name='Tripadvisor URL'),
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter URL'),
        ),
    ]
