# Generated by Django 2.2.7 on 2020-05-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
