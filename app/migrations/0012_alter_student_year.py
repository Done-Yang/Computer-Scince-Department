# Generated by Django 4.1.2 on 2023-02-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
