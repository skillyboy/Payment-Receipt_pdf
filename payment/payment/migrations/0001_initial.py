# Generated by Django 4.0.6 on 2022-07-24 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=50)),
                ('answer1', models.CharField(max_length=50)),
                ('answer2', models.CharField(blank=True, max_length=50, null=True)),
                ('answer3', models.CharField(blank=True, max_length=50, null=True)),
                ('answer4', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'log',
                'verbose_name_plural': 'logs',
                'db_table': 'log',
                'managed': True,
            },
        ),
    ]