# Generated by Django 4.0.5 on 2022-07-16 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0024_childrensundayschool_adultsundayschool'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('title', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('name2', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(null=True)),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
