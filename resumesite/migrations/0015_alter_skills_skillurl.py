# Generated by Django 3.2.9 on 2021-11-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0014_skills_skillurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skillurl',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Skill Logo URL'),
        ),
    ]