# Generated by Django 4.0.6 on 2022-07-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_transaction_date_transaction_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='unique_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]