# Generated by Django 3.1.6 on 2021-03-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_auto_20210326_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Account_no',
            field=models.IntegerField(),
        ),
    ]