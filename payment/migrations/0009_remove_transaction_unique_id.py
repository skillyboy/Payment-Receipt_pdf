# Generated by Django 4.0.6 on 2022-07-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_processor_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='unique_id',
        ),
    ]
