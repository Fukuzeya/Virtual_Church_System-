# Generated by Django 3.1 on 2022-06-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_auto_20220609_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
    ]
