# Generated by Django 4.0.5 on 2022-07-17 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0029_historyofbabalola'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryOfCAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(null=True)),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
