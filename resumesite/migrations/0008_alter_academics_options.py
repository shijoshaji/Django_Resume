# Generated by Django 3.2.9 on 2021-11-05 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0007_alter_academics_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academics',
            options={'ordering': ['-year_of_passing']},
        ),
    ]
