# Generated by Django 3.1.6 on 2021-03-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0003_auto_20210327_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('3', 'completed'), ('1', 'yettobegin'), ('2', 'progress')], max_length=120),
        ),
        migrations.AlterField(
            model_name='batch',
            name='course_image',
            field=models.ImageField(null=True, upload_to='image1'),
        ),
    ]
