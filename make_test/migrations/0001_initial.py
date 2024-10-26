# Generated by Django 5.1.2 on 2024-10-26 11:52

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='F.I.Sh')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefon raqam')),
                ('telegram_id', models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Telegram ID')),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('user', 'Oddiy foydalanuvchi')], default='user', max_length=100, null=True, verbose_name='Foydalanuvchi roli')),
                ('joined_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 26, 16, 52, 27, 781367), null=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Foydalanuvchilar',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=221, null=True, verbose_name='Nomi')),
                ('file', models.FileField(blank=True, null=True, upload_to='texts/', verbose_name='Test Excel fayli')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 26, 16, 52, 27, 781367), null=True, verbose_name='Yaratilgan vaqti')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='make_test.users', verbose_name='Test egasi')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Testlar',
                'db_table': 'Contest',
            },
        ),
        migrations.CreateModel(
            name='Versions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=221, null=True, verbose_name='Nomi')),
                ('tests_file', models.FileField(blank=True, null=True, upload_to='versions/', verbose_name='Tuzilgan testlar fayli')),
                ('answers_file', models.FileField(blank=True, null=True, upload_to='answers/', verbose_name='Test javoblari')),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 26, 16, 52, 27, 781367), null=True, verbose_name='Yaratilgan vaqti')),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='make_test.test', verbose_name='Test')),
            ],
            options={
                'verbose_name': 'Version',
                'verbose_name_plural': 'Test versiyasi',
                'db_table': 'Version',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation', models.CharField(blank=True, max_length=221, null=True, verbose_name='Variant')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 26, 16, 52, 27, 797006), null=True, verbose_name='Tekshirilgan vaqti')),
                ('test_version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='make_test.versions', verbose_name='Test versiyasi nomi')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Natijalar',
                'db_table': 'Results',
            },
        ),
    ]
