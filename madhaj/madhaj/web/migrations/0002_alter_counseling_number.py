# Generated by Django 4.0.6 on 2022-07-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counseling',
            name='number',
            field=models.IntegerField(),
        ),
    ]