# Generated by Django 3.2.25 on 2025-04-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofproject',
            name='type_of_work',
            field=models.CharField(max_length=50),
        ),
    ]
