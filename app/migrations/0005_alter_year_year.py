# Generated by Django 4.1.2 on 2023-02-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_years_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(choices=[(1, 'Year1'), (2, 'Year2'), (3, 'Year3')], max_length=30),
        ),
    ]
