# Generated by Django 3.1.6 on 2021-03-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_purchase', models.CharField(max_length=120)),
                ('purchase_price', models.CharField(max_length=50)),
                ('selling_price', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.item')),
            ],
        ),
    ]
