# Generated by Django 4.0.6 on 2022-07-25 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'processor',
                'verbose_name_plural': 'processors',
                'db_table': 'processor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('pending_transactions', models.CharField(blank=True, max_length=50, null=True)),
                ('paid_transactions', models.CharField(blank=True, max_length=50, null=True)),
                ('total_paid_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_code', models.CharField(max_length=50)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.processor')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
                'db_table': 'transaction',
                'managed': True,
            },
        ),
    ]
