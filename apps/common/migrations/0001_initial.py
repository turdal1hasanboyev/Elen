# Generated by Django 5.1.7 on 2025-03-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_email', models.EmailField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Sub Email',
                'verbose_name_plural': 'Sub Emails',
            },
        ),
    ]
