# Generated by Django 3.1 on 2022-06-09 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_auto_20220609_1454'),
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting_candidate',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='voting_candidate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Private_Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.CharField(choices=[("Women's Fellowship", "Women's Fellowship"), ("Men's Fellowship", "Men's Fellowship"), ("Youth's Fellowship", "Youth's Fellowship"), ("Children's Ministry", "Children's Ministry"), ("Couple's Ministry", "Couple's Ministry"), ('Widows and Singles Ministry', 'Widows and Singles Ministry'), ('Intercession Team', 'Intercession Team'), ('Building Commission', 'Building Commission'), ('Fundraising Commission', 'Fundraising Commission'), ('Ushering Commision', 'Ushering Commision'), ('Praise Team', 'Praise Team'), ('Evangelism and Outreach Commission', 'Evangelism and Outreach Commission'), ('Health Commission', 'Health Commission'), ('Finance Commission', 'Finance Commission'), ('Pastor and Wife', 'Pastor and Wife'), ('Elders', 'Elders'), ('Decons and Deconnesses', 'Decons and Deconnesses')], max_length=100)),
                ('meeting_title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='meetings', to='Management.members')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting_Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='private_meeting_members', to='Dashboard.private_meetings')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_members', to='Management.members')),
            ],
        ),
    ]
