# Generated by Django 3.1.6 on 2021-03-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0018_auto_20210331_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_id',
            field=models.CharField(editable=False, max_length=120, primary_key=True, serialize=False),
        ),
    ]