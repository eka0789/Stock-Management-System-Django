# Generated by Django 3.1.5 on 2021-01-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0006_stock_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
