# Generated by Django 3.2.9 on 2021-11-09 06:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0018_about_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='intro',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='One Line Intro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='desp',
            field=models.TextField(max_length=2000, verbose_name='About Me'),
        ),
    ]
