# Generated by Django 3.1.12 on 2022-05-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('national_id', models.CharField(max_length=12, unique=True)),
                ('contact', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=25)),
                ('commission', models.CharField(choices=[("Women's Fellowship", "Women's Fellowship"), ("Men's Fellowship", "Men's Fellowship"), ("Youth's Fellowship", "Youth's Fellowship"), ("Children's Ministry", "Children's Ministry"), ("Couple's Ministry", "Couple's Ministry"), ('Widows and Singles Ministry', 'Widows and Singles Ministry'), ('Intercession Team', 'Intercession Team'), ('Building Commission', 'Building Commission'), ('Fundraising Commission', 'Fundraising Commission'), ('Ushering Commision', 'Ushering Commision'), ('Praise Team', 'Praise Team'), ('Evangelism and Outreach Commission', 'Evangelism and Outreach Commission'), ('Health Commission', 'Health Commission'), ('Finance Commission', 'Finance Commission'), ('Pastor and Wife', 'Pastor and Wife'), ('Elders', 'Elders'), ('Decons and Deconnesses', 'Decons and Deconnesses')], max_length=50)),
                ('occupation', models.CharField(max_length=25)),
                ('leadership_position', models.CharField(choices=[('Elder', 'Elder'), ('Chairperson', 'Chairperson'), ('Decon', 'Decon'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Member', 'Member')], max_length=25)),
                ('location', models.CharField(choices=[('Area 3', 'Area 3'), ('Area C', 'Area C'), ('Area 12', 'Area 12'), ('Area 13', 'Area 13'), ('Area 14', 'Area 14'), ('Area 16', 'Area 16'), ('Two Rooms', 'Two Rooms'), ('Destiny', 'Destiny')], max_length=25)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=25)),
                ('status', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]