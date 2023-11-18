# Generated by Django 4.2.6 on 2023-11-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=1000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('publish', models.BooleanField(default=0)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='posts/image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
