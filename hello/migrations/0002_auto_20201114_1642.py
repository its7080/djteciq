# Generated by Django 3.1.2 on 2020-11-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]