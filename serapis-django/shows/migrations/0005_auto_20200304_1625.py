# Generated by Django 3.0.3 on 2020-03-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20200304_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='new_venue',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]