# Generated by Django 5.0.2 on 2024-04-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsolo', '0003_mobile_internet'),
    ]

    operations = [
        migrations.CreateModel(
            name='television',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
