# Generated by Django 4.0.5 on 2022-06-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded'),
        ),
    ]