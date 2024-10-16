# Generated by Django 5.1.1 on 2024-10-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('skills', models.TextField(blank=True, null=True)),
                ('detail_url', models.URLField()),
                ('end_date', models.CharField(default='상시 채용', max_length=100)),
                ('platform_name', models.CharField(default='Jobplanet', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
