# Generated by Django 3.1 on 2022-06-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]