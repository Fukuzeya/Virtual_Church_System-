# Generated by Django 3.1 on 2022-06-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20220609_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting_candidate',
            name='voting_closed',
            field=models.BooleanField(default=False),
        ),
    ]
