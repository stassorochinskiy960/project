# Generated by Django 3.2.25 on 2025-04-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_alter_quoterequest_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoterequest',
            name='address',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='quoterequest',
            name='contact_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='quoterequest',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='quoterequest',
            name='phone_number',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
