# Generated by Django 4.0.5 on 2022-07-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0019_sundaysermon'),
    ]

    operations = [
        migrations.AddField(
            model_name='sundaysermon',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sundaysermon',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
