# Generated by Django 4.2.1 on 2023-06-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default='Не указан', max_length=12)),
            ],
        ),
    ]
