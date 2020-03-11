# Generated by Django 2.1 on 2019-10-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20190917_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthregistration',
            name='id_no',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='birthregistration',
            name='reference_number',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]