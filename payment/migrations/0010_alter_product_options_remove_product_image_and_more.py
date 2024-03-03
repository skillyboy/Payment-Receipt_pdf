# Generated by Django 4.0.6 on 2022-07-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_remove_transaction_unique_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name': 'sub', 'verbose_name_plural': 'sub'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='fee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='sub',
        ),
    ]
