# Generated by Django 3.0.3 on 2020-03-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0021_auto_20200326_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_photo')),
                ('name', models.CharField(default='name', max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]