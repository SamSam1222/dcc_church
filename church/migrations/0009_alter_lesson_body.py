# Generated by Django 4.0.5 on 2022-07-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0008_alter_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='body',
            field=models.TextField(blank=True, max_length=500, verbose_name='body'),
        ),
    ]
