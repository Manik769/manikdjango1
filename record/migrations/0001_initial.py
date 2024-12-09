# Generated by Django 5.1.2 on 2024-11-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('language', models.CharField(choices=[('spanish', 'Spanish'), ('french', 'French'), ('english', 'English')], max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
