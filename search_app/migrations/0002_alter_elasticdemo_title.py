# Generated by Django 4.1 on 2023-09-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elasticdemo',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
