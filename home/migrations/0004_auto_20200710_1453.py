# Generated by Django 3.0.7 on 2020-07-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200710_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='contact',
            name='wesite',
            field=models.CharField(default='', max_length=122),
        ),
    ]
