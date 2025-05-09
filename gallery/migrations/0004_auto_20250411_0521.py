# Generated by Django 3.2.25 on 2025-04-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_ad1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos/advertize')),
                ('link', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Annonsment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Ad1',
        ),
    ]
