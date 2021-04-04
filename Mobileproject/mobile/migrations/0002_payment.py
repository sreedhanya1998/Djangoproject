# Generated by Django 3.1.6 on 2021-03-26 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_no', models.CharField(max_length=18)),
                ('IFSC_code', models.CharField(max_length=50)),
                ('Amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.mobileorder')),
            ],
        ),
    ]
