# Generated by Django 3.0.3 on 2021-07-11 15:32

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_string', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_by', models.BigIntegerField(blank=True, null=True)),
                ('updated_by', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
