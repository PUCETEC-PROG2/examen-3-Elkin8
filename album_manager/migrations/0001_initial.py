# Generated by Django 4.2 on 2024-08-07 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(max_length=10)),
                ('gender', models.CharField(choices=False, max_length=30)),
                ('picture', models.ImageField(upload_to='album_images')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album_manager.artist')),
            ],
        ),
    ]
