# Generated by Django 2.0.4 on 2018-04-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20180411_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='yeasr',
            field=models.CharField(default='1/25xx', max_length=6),
        ),
    ]
